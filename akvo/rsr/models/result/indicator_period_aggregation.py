# -*- coding: utf-8 -*-

# Akvo Reporting is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from django.db import models

from django_pgviews import view as pg


ACTUAL_VALUE_SQL = """
    SELECT
        -- row_number() OVER... creates an artificial "pk" column, without which Django will protest
        row_number() OVER (ORDER BY period.id) AS id,
        period.id AS period_id,
        indicator.measure as measure,
        sum((update.value) :: DECIMAL(20,2)) AS value,
        sum((update.numerator) :: DECIMAL(20,2)) AS numerator,
        sum((update.denominator) :: DECIMAL(20,2)) AS denominator
    FROM
        rsr_indicatorperiod period,
        rsr_indicator indicator,
        rsr_indicatorperioddata update
    WHERE
        (
            (((indicator.id = period.indicator_id) AND
            (period.id = update.period_id)) AND
            ((update.status) :: TEXT = 'A' :: TEXT)) AND
            ((update.value) :: TEXT ~ '^\d+\.?\d{0,2}$' :: TEXT OR update.value IS NULL)
        )
    GROUP BY period.id, indicator.measure;
"""


class PeriodActualValue(pg.View):
    # on_delete=models.DO_NOTHING is needed to prevent problems with PG trying to delete views' data
    period = models.ForeignKey('IndicatorPeriod', on_delete=models.DO_NOTHING)
    measure = models.CharField(max_length=1)
    value = models.IntegerField()
    numerator = models.IntegerField()
    denominator = models.IntegerField()

    sql = ACTUAL_VALUE_SQL

    class Meta:
        app_label = 'rsr'
        db_table = 'rsr_indicator_period_actual_value'
        managed = False


DISAGG_SQL = """
    WITH aggregated_disaggs AS (
        SELECT
            disagg.dimension_id AS dimension_id,
            sum((disagg.value) :: DECIMAL(20,2)) AS value,
            sum((disagg.numerator) :: DECIMAL(20,2)) AS numerator,
            sum((disagg.denominator) :: DECIMAL(20,2)) AS denominator
        FROM
            rsr_disaggregation disagg,
            rsr_indicatorperioddata "update"
        WHERE
            update.status = 'A' AND
            disagg.update_id = update.id
        GROUP BY
            dimension_id
    ),
    period_disaggs AS (
        SELECT DISTINCT
            indicator.id AS indicator_id,
            period.id AS period_id,
            dimension.name AS dimension_name,
            dimension.value AS dimension_value,
            agg.value,
            agg.numerator,
            agg.denominator
        FROM
            rsr_indicator indicator,
            rsr_indicatorperiod period,
            rsr_indicatorperioddata update,
            aggregated_disaggs agg,
            rsr_indicatordimension dimension
        WHERE
            indicator.id = period.indicator_id AND
            period.id = update.period_id AND
            indicator.id = dimension.indicator_id AND
            dimension.id = agg.dimension_id
    )
    SELECT
        row_number() OVER (ORDER BY indicator_id) AS id,
        *
    FROM period_disaggs
"""


class PeriodDisaggregation(pg.View):
    indicator = models.ForeignKey('Indicator', on_delete=models.DO_NOTHING)
    period = models.ForeignKey('IndicatorPeriod', on_delete=models.DO_NOTHING)
    dimension_name = models.CharField(max_length=100)
    dimension_value = models.CharField(max_length=100)
    value = models.IntegerField()
    numerator = models.IntegerField()
    denominator = models.IntegerField()

    sql = DISAGG_SQL

    class Meta:
        app_label = 'rsr'
        db_table = 'rsr_indicator_period_disaggregation'
        managed = False
