# -*- coding: utf-8 -*-

# Akvo Reporting is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from unittest import TestCase

from django.contrib.auth import get_user_model

from akvo.rsr.models import Project
from akvo.rsr.models import ProjectUpdate


class ProjectModelTestCase(TestCase):
    """Tests for the project model"""

    def test_project_last_update(self):
        """Test that Project.last_update is updated correctly when an update is deleted.

        The field is a denormalization keeping track of the latest update for a project, if any.
        When deletion of updates was introduced, a bug occurs when deleting the latest update, as
        the Project.last_update field was set to None in that case.
        The tests check that the fix for this bug works correctly.
        """
        # setup needed model instances
        project_1 = Project.objects.create(title="Test project 1")
        user_1 = get_user_model().objects.create(email='user1@com.com')
        update_1 = ProjectUpdate.objects.create(title="Test update 1", project=project_1, user=user_1)
        update_2 = ProjectUpdate.objects.create(title="Test update 2", project=project_1, user=user_1)

        # check that update_2 is the latest
        self.assertTrue(update_1.created_at < update_2.created_at)

        # check that update_2 is Project.last_update
        self.assertEqual(project_1.last_update, update_2)

        update_2.delete()
        # now update_1 should be last_update
        self.assertEqual(project_1.last_update, update_1)

        update_1.delete()
        # now last_update is None
        self.assertEqual(project_1.last_update, None)