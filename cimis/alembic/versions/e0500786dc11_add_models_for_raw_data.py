"""add models for raw data

Revision ID: e0500786dc11
Revises: b4241cfddd05
Create Date: 2021-06-15 12:23:24.991593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'e0500786dc11'
down_revision = 'b4241cfddd05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('DailyRaw',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Date', sa.Date(), nullable=False),
    sa.Column('DayAirTmpAvg', sa.Float(), nullable=True),
    sa.Column('DayAirTmpAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DayAirTmpAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DayAirTmpMax', sa.Float(), nullable=True),
    sa.Column('DayAirTmpMaxQc', sa.String(length=50), nullable=True),
    sa.Column('DayAirTmpMaxUnits', sa.String(length=50), nullable=True),
    sa.Column('DayAirTmpMin', sa.Float(), nullable=True),
    sa.Column('DayAirTmpMinQc', sa.String(length=50), nullable=True),
    sa.Column('DayAirTmpMinUnits', sa.String(length=50), nullable=True),
    sa.Column('DayDewPnt', sa.Float(), nullable=True),
    sa.Column('DayDewPntQc', sa.String(length=50), nullable=True),
    sa.Column('DayDewPntUnits', sa.String(length=50), nullable=True),
    sa.Column('DayEto', sa.Float(), nullable=True),
    sa.Column('DayEtoQc', sa.String(length=50), nullable=True),
    sa.Column('DayEtoUnits', sa.String(length=50), nullable=True),
    sa.Column('DayAsceEto', sa.Float(), nullable=True),
    sa.Column('DayAsceEtoQc', sa.String(length=50), nullable=True),
    sa.Column('DayAsceEtoUnits', sa.String(length=50), nullable=True),
    sa.Column('DayAsceEtr', sa.Float(), nullable=True),
    sa.Column('DayAsceEtrQc', sa.String(length=50), nullable=True),
    sa.Column('DayAsceEtrUnits', sa.String(length=50), nullable=True),
    sa.Column('DayPrecip', sa.Float(), nullable=True),
    sa.Column('DayPrecipQc', sa.String(length=50), nullable=True),
    sa.Column('DayPrecipUnits', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumAvg', sa.Float(), nullable=True),
    sa.Column('DayRelHumAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumMax', sa.Float(), nullable=True),
    sa.Column('DayRelHumMaxQc', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumMaxUnits', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumMin', sa.Float(precision=50), nullable=True),
    sa.Column('DayRelHumMinQc', sa.String(length=50), nullable=True),
    sa.Column('DayRelHumMinUnits', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpAvg', sa.Float(), nullable=True),
    sa.Column('DaySoilTmpAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpMax', sa.Float(), nullable=True),
    sa.Column('DaySoilTmpMaxQc', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpMaxUnits', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpMin', sa.Float(), nullable=True),
    sa.Column('DaySoilTmpMinQc', sa.String(length=50), nullable=True),
    sa.Column('DaySoilTmpMinUnits', sa.String(length=50), nullable=True),
    sa.Column('DaySolRadAvg', sa.Float(), nullable=True),
    sa.Column('DaySolRadAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DaySolRadAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DaySolRadNet', sa.Float(), nullable=True),
    sa.Column('DaySolRadNetQc', sa.String(length=50), nullable=True),
    sa.Column('DaySolRadNetUnits', sa.String(length=50), nullable=True),
    sa.Column('DayVapPresAvg', sa.Float(), nullable=True),
    sa.Column('DayVapPresAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DayVapPresAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DayVapPresMax', sa.Float(), nullable=True),
    sa.Column('DayVapPresMaxQc', sa.String(length=50), nullable=True),
    sa.Column('DayVapPresMaxUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindEne', sa.Float(), nullable=True),
    sa.Column('DayWindEneQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindEneUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindEse', sa.Float(), nullable=True),
    sa.Column('DayWindEseQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindEseUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindNne', sa.Float(), nullable=True),
    sa.Column('DayWindNneQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindNneUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindNnw', sa.Float(), nullable=True),
    sa.Column('DayWindNnwQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindNnwUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindRun', sa.Float(), nullable=True),
    sa.Column('DayWindRunQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindRunUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindSpdAvg', sa.Float(), nullable=True),
    sa.Column('DayWindSpdAvgQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindSpdAvgUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindSsw', sa.Float(), nullable=True),
    sa.Column('DayWindSswQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindSswUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindSse', sa.Float(), nullable=True),
    sa.Column('DayWindSseQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindSseUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindWnw', sa.Float(), nullable=True),
    sa.Column('DayWindWnwQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindWnwUnits', sa.String(length=50), nullable=True),
    sa.Column('DayWindWsw', sa.Float(), nullable=True),
    sa.Column('DayWindWswQc', sa.String(length=50), nullable=True),
    sa.Column('DayWindWswUnits', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('HourlyRaw',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Date', sa.Date(), nullable=False),
    sa.Column('Hour', sa.Time(), nullable=False),
    sa.Column('HlyAirTmp', sa.Float(), nullable=True),
    sa.Column('HlyAirTmpQc', sa.String(length=50), nullable=True),
    sa.Column('HlyAirTmpUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyDewPnt', sa.Float(), nullable=True),
    sa.Column('HlyDewPntQc', sa.String(length=50), nullable=True),
    sa.Column('HlyDewPntUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyEto', sa.Float(), nullable=True),
    sa.Column('HlyEtoQc', sa.String(length=50), nullable=True),
    sa.Column('HlyEtoUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyNetRad', sa.Float(), nullable=True),
    sa.Column('HlyNetRadQc', sa.String(length=50), nullable=True),
    sa.Column('HlyNetRadUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyAsceEto', sa.Float(), nullable=True),
    sa.Column('HlyAsceEtoQc', sa.String(length=50), nullable=True),
    sa.Column('HlyAsceEtoUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyAsceEtr', sa.Float(), nullable=True),
    sa.Column('HlyAsceEtrQc', sa.String(length=50), nullable=True),
    sa.Column('HlyAsceEtrUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyPrecip', sa.Float(), nullable=True),
    sa.Column('HlyPrecipQc', sa.String(length=50), nullable=True),
    sa.Column('HlyPrecipUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyRelHum', sa.Float(), nullable=True),
    sa.Column('HlyRelHumQc', sa.String(length=50), nullable=True),
    sa.Column('HlyRelHumUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyResWind', sa.Float(), nullable=True),
    sa.Column('HlyResWindQc', sa.String(length=50), nullable=True),
    sa.Column('HlyResWindUnits', sa.String(length=50), nullable=True),
    sa.Column('HlySoilTmp', sa.Float(), nullable=True),
    sa.Column('HlySoilTmpQc', sa.String(length=50), nullable=True),
    sa.Column('HlySoilTmpUnits', sa.String(length=50), nullable=True),
    sa.Column('HlySolRad', sa.Float(), nullable=True),
    sa.Column('HlySolRadQc', sa.String(length=50), nullable=True),
    sa.Column('HlySolRadUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyVapPres', sa.Float(), nullable=True),
    sa.Column('HlyVapPresQc', sa.String(length=50), nullable=True),
    sa.Column('HlyVapPresUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyWindDir', sa.Float(), nullable=True),
    sa.Column('HlyWindDirQc', sa.String(length=50), nullable=True),
    sa.Column('HlyWindDirUnits', sa.String(length=50), nullable=True),
    sa.Column('HlyWindSpd', sa.Float(), nullable=True),
    sa.Column('HlyWindSpdQc', sa.String(length=50), nullable=True),
    sa.Column('HlyWindSpdUnits', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('HourlyRaw')
    op.drop_table('DailyRaw')
    # ### end Alembic commands ###
