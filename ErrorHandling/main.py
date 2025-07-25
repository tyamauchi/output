from fastapi import FastAPI
from fastapi.responses import JSONResponse
from functools import partial
from pydantic import BaseModel

app = FastAPI()

# Pydantic モデルでレスポンス構造を定義
class ResultModel(BaseModel):
    result: str

def func_c():
    raise ValueError("func_cでエラー発生")

def func_d():
    func_c()

def func_b():
    func_d()

def func_a():
    try:
        # func_b を partial で呼び出す
        partial_func = partial(func_b)
        partial_func()
        return "正常終了"
    except ValueError as e:
        return f"エラー発生: {str(e)}"

@app.get("/", response_model=ResultModel)
async def root():
    best_solution = func_a()
    return {"result": best_solution}
