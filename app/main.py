from functools import lru_cache

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hey! I am fibonacci sequence"}


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@app.get("/fibonacci")
def get_fibonacci(n: int):
    fibo = fib(n)
    return {
        "message": "Query successful",
        "number": n,
        "nth_term": fibo
    }
