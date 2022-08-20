from pydantic import BaseModel, ValidationError, validator, Field
from pydantic.utils import Optional

class MetricInfo(BaseModel):
    tn: Optional[int]
    fp: Optional[int]
    fn: Optional[int]
    tp: Optional[int]

    precision: Optional[float]
    recall: Optional[float]
    fbeta: Optional[float]