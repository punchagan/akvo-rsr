# -*- coding: utf-8 -*-

"""
Akvo RSR is covered by the GNU Affero General Public License.

See more details in the license.txt file located at the root folder of the Akvo RSR module.
For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.
"""

import json
import os

from django.conf import settings
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.test import TestCase, Client

from akvo.rsr.iso3166 import ISO_3166_COUNTRIES
from akvo.rsr.models import (Project, Organisation, Partnership, User,
                             Employment, Keyword, PartnerSite,
                             PublishingStatus, ProjectLocation, Country,
                             RecipientCountry)


class RestProjectTestCase(TestCase):
    """Tests the project REST endpoints."""

    def setUp(self):
        """
        For all tests, we at least need two projects in the database. And a client.
        """
        project = Project.objects.create(
            title="REST test project",
        )
        project.publish()
        self.project = Project.objects.create(
            title="REST test project 2",
        )
        self.project.publish()

        # Create organisation
        self.reporting_org = Organisation.objects.create(
            id=1337,
            name="Test REST reporting",
            long_name="Test REST reporting org",
            new_organisation_type=22
        )

        self.c = Client(HTTP_HOST=settings.RSR_DOMAIN)

    def test_rest_project(self):
        """
        Checks the regular REST project endpoint.
        """
        response = self.c.get('/rest/v1/project/', {'format': 'json'})
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], 2)

    def test_rest_project_reporting_org(self):
        """
        Checks the regular REST project endpoint with the 'reporting_org' or 'partnerships'
        parameter.
        """
        Partnership.objects.create(
            project=self.project,
            organisation=self.reporting_org,
            iati_organisation_role=Partnership.IATI_REPORTING_ORGANISATION,
        )

        response = self.c.get('/rest/v1/project/', {'format': 'json', 'reporting_org': 1337})
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], 1)

        response = self.c.get('/rest/v1/project/', {'format': 'json', 'partnerships__exact': 1234})
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], 0)

    def test_rest_project_iati_export_reporting_org(self):
        """
        Checks the regular REST project endpoint with the reporting org parameter.
        """
        Partnership.objects.create(
            project=self.project,
            organisation=self.reporting_org,
            iati_organisation_role=Partnership.IATI_REPORTING_ORGANISATION,
        )

        response = self.c.get('/rest/v1/project_iati_export/', {'format': 'json',
                                                                'reporting_org': 1337})
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], 1)

    def test_rest_project_wrong_filter(self):
        """
        Checks the regular REST project endpoint with a non-existing filter.
        """
        Partnership.objects.create(
            project=self.project,
            organisation=self.reporting_org,
            iati_organisation_role=Partnership.IATI_REPORTING_ORGANISATION,
        )

        response = self.c.get('/rest/v1/project_iati_export/', {'format': 'json',
                                                                'wrong__exact': 'parameter'})
        self.assertEqual(response.status_code, 200)

    def test_rest_project_advanced_filters(self):
        """
        Checks the regular REST project endpoint with advanced filters and options.
        """
        # Correct request
        response = self.c.get('/rest/v1/project/', {'format': 'json',
                                                    'filter': "{'title__icontains':'water'}",
                                                    'exclude': "{'currency':'EUR'}",
                                                    'prefetch_related': "['partners']"})
        self.assertEqual(response.status_code, 200)

        # Incorrect request
        response = self.c.get('/rest/v1/project/', {'format': 'json',
                                                    'filter': "{'blabla__icontains':'water'}",
                                                    'exclude': "{'currency':'EUR'}",
                                                    'prefetch_related': "['partners']"})
        self.assertEqual(response.status_code, 500)

        # Request with the Q object
        response = self.c.get('/rest/v1/project/', {'format': 'json',
                                                    'q_filter1': "{'title__icontains':'water'}",
                                                    'q_filter2': "{'currency':'EUR'}"})
        self.assertEqual(response.status_code, 200)

    def test_rest_project_permissions(self):
        """
        Checks the access to projects for a logged in non-superuser. Also for private projects.
        """
        # Create necessary groups
        for group in settings.REQUIRED_AUTH_GROUPS:
            Group.objects.get_or_create(name=group)
        admin_group, _created = Group.objects.get_or_create(name="Admins")

        # Create project
        new_project = Project.objects.create(
            title="Private project",
            is_public=False,
        )

        # Create partnership
        Partnership.objects.create(
            project=new_project,
            organisation=self.reporting_org,
            iati_organisation_role=Partnership.IATI_REPORTING_ORGANISATION,
        )

        # Create active user
        user = User.objects.create_user(
            username="Normal user REST",
            email="user.rest@test.akvo.org",
            password="password",
        )
        user.is_active = True
        user.save()

        # Create employment
        Employment.objects.create(
            user=user,
            organisation=self.reporting_org,
            group=admin_group,
            is_approved=True,
        )

        self.c.login(username=user.username, password="password")

        response = self.c.get('/rest/v1/project/', {'format': 'json'})
        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertEqual(content['count'], 3)


class ProjectDirectoryTestCase(TestCase):

    def setUp(self):
        super(ProjectDirectoryTestCase, self).setUp()
        self.organisation = self._create_organisation('Akvo')
        self.partner_site = PartnerSite.objects.create(
            organisation=self.organisation,
            piwik_id=1,
            hostname='akvo'
        )

        self.image = os.path.join(settings.MEDIA_ROOT, 'test-image.png')
        with open(self.image, 'w+b'):
            pass

        for i in range(1, 6):
            project = Project.objects.create(title='Project - {}'.format(i),
                                             current_image=self.image)
            if i < 4:
                publishing_status = project.publishingstatus
                publishing_status.status = PublishingStatus.STATUS_PUBLISHED
                publishing_status.save()

            # Add a partnership for a couple of projects
            if i in {1, 4}:
                Partnership.objects.create(
                    organisation=self.organisation,
                    project=project,
                    iati_organisation_role=Partnership.IATI_REPORTING_ORGANISATION
                )

        # Additional organisation for typeahead/organisations end-point
        self._create_organisation('UNICEF')

    def tearDown(self):
        os.remove(self.image)
        cache.clear()

    def _create_client(self, host=None):
        """ Create and return a client with the given host."""
        if not host:
            host = settings.RSR_DOMAIN
        return Client(HTTP_HOST=host)

    def _create_organisation(self, name):
        long_name = '{} organisation'.format(name)
        return Organisation.objects.create(name=name, long_name=long_name)

    def test_should_show_keyword_projects_in_partner_site(self):
        # Given
        hostname = 'akvo'
        host = '{}.{}'.format(hostname, settings.AKVOAPP_DOMAIN)
        partner_projects = False
        keyword = Keyword.objects.create(label=hostname)
        self.partner_site.partner_projects = partner_projects
        self.partner_site.save()
        self.partner_site.keywords.add(keyword)
        project_title = '{} awesome project'.format(hostname)
        project = Project.objects.create(title=project_title, current_image=self.image)
        project.keywords.add(keyword)
        project.publish()

        url = '/rest/v1/project_directory?format=json'
        client = self._create_client(host)

        # When
        response = client.get(url, follow=True)

        # Then
        self.assertEqual(len(response.data['projects']), 1)
        self.assertEqual(project_title, response.data['projects'][0]['title'])

    def test_should_show_all_partner_projects(self):
        # Given
        hostname = 'akvo'
        host = '{}.{}'.format(hostname, settings.AKVOAPP_DOMAIN)
        url = '/rest/v1/project_directory?format=json'
        client = self._create_client(host)

        # When
        response = client.get(url, follow=True)

        # Then
        self.assertEqual(len(response.data['projects']), 1)
        self.assertIn('Project - 1', response.data['projects'][0]['title'])

    def test_should_show_all_country_projects(self):
        # Given
        titles = ['Project - {}'.format(i) for i in range(0, 6)]
        projects = [None] + [Project.objects.get(title=title) for title in titles[1:]]
        url = '/rest/v1/project_directory?format=json&location=262'
        latitude, longitude = ('11.8948112', '42.5807153')
        country_code = 'DJ'
        # Add a Recipient Country - DJ
        RecipientCountry.objects.create(project=projects[2], country=country_code)
        # ProjectLocation in DJ
        self.setup_country_objects()
        project_location = ProjectLocation.objects.create(location_target=projects[3],
                                                          latitude=latitude,
                                                          longitude=longitude)
        project_location = ProjectLocation.objects.create(location_target=projects[4],
                                                          latitude=latitude,
                                                          longitude=longitude)
        project_location = ProjectLocation.objects.create(location_target=projects[5],
                                                          latitude=latitude,
                                                          longitude=longitude)

        # ProjectLocation with no country
        ProjectLocation.objects.create(location_target=projects[3],
                                       latitude=None,
                                       longitude=None)
        client = self._create_client()

        # When
        response = client.get(url, follow=True)

        # Then
        projects = response.data['projects']
        self.assertEqual(len(projects), 2)
        response_titles = {project['title'] for project in projects}
        self.assertIn(titles[2], response_titles)
        self.assertIn(titles[3], response_titles)
        self.assertEqual(project_location.country.iso_code, country_code.lower())

    def setup_country_objects(self):
        for iso_code, name in ISO_3166_COUNTRIES:
            Country.objects.create(name=name, iso_code=iso_code)
