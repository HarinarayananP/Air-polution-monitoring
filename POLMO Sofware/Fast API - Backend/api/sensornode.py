from fastapi import Depends, HTTPException, APIRouter, BackgroundTasks, Header
from starlette import status

from models.sensordata import SensorReading
from services.sensor import get_last_value

r = APIRouter()

valid_sensors = ['NO2', 'CO2', 'CH4', 'CO', 'PM1.0', 'PM2.0', 'PM10', 'O3', 'SO2']


@r.get('/sensor/{node}/{pollutant}/last/', response_model=SensorReading, tags=['SensorNode'])
async def get_last_reading(node: str, pollutant: str):
    if pollutant not in valid_sensors:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Sensor name is invalid")
    res = await get_last_value(pollutant, node)
    if not res:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT, detail="No data available")
    return res

