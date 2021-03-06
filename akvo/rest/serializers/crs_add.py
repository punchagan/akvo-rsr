# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from akvo.rsr.models import CrsAdd, CrsAddOtherFlag

from .rsr_serializer import BaseRSRSerializer

from rest_framework import serializers


class CrsAddSerializer(BaseRSRSerializer):

    repayment_type_label = serializers.ReadOnlyField(source='iati_repayment_type_unicode')
    repayment_plan_label = serializers.ReadOnlyField(source='iati_repayment_plan_unicode')
    currency_label = serializers.ReadOnlyField(source='iati_currency_unicode')
    channel_code_label = serializers.ReadOnlyField(source='iati_channel_code_unicode')

    class Meta:
        model = CrsAdd


class CrsAddOtherFlagSerializer(BaseRSRSerializer):

    code_label = serializers.ReadOnlyField(source='iati_code_unicode')

    class Meta:
        model = CrsAddOtherFlag
