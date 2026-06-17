from fastapi import APIRouter
from services.parquet_orchestrator_service import get_h3_indexed_file_paths

test_router = APIRouter(prefix="/test", tags=["test"])

@test_router.get("/h3_index_in_tile/{z}/{x}/{y}")
def get_h3_index_in_tile(z:int, x:int, y:int):
    h3_index_file_paths  = get_h3_indexed_file_paths(z,x,y)
    return { "h3_index_file_paths": h3_index_file_paths}
