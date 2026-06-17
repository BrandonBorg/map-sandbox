from fastapi import APIRouter
from services.parquet_orchestrator_service import get_h3_indexs_for_tile

test_router = APIRouter(prefix="/test", tags=["test"])

@test_router.get("/h3_index_in_tile/{z}/{x}/{y}")
def get_h3_index_in_tile(z:int, x:int, y:int):
    h3_indexs  = get_h3_indexs_for_tile(z,x,y)
    print({"t":h3_indexs})
    return {"h3_indexs":h3_indexs}
