from functools import lru_cache

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hey! I am fibonacci sequence"}


@lru_cache(maxsize=512)
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@app.get("/fibonacci")
def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")
    if n > 500:
        raise HTTPException(status_code=400, detail="n must be 500 or less to avoid recursion limits")
    fibo = fib(n)
    return {
        "message": "Query successful",
        "number": n,
        "nth_term": fibo
    }
