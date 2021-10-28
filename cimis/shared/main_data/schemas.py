from typing import Any

import pydantic

# Daily Raw Data Schemas

class Sister(pydantic.BaseModel):

    class Config:
        extra = 'ignore'
    
    StationId: int
    FirstSisterId: int
    SecondSisterId: int

    def __eq__(self, other: Any) -> bool:
        return all(
            [
                isinstance(other, Sister)
            ]
        )