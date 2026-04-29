from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hey! I am fibonacci sequence"}


# Implementing the nth term of a fibonacci sequence
# Using the formula F(n) = F(n-1) + F(n-2)

def fib(n: int) -> int:
    """Helper function to calculate fibonacci number recursively."""
    if n == 0:  # first term of the sequence
        return 0
    if n == 1:  # second term of the sequence
        return 1
    return fib(n - 1) + fib(n - 2)  # F(n) = F(n-1) + F(n-2)


@app.get("/fibonacci")
def get_fibonacci(n: int):
    """Endpoint to find the nth term of the fibonacci sequence."""
    fibo = fib(n)
    return {
        "message": "Query successful",
        "number": n,
        "nth_term": fibo
    }



# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")

# def index():
#     return "Hey! I am fibonacci sequence"


# # We would be implementing the code for determing the nth term of a fibonacci sequence
# # We would be implementing this code using the F(n) = F(n-1) + F(n-2)

# @app.get("/fibonacci")
# def fib(n): 
#     # where n is the number we want to find from the sequence. 

#     # Let predetermine the first and second term of the sequence,{0, 1, .....}
#     if n == 0: # for the forst term of the sequence.
#         return 0
#     if n == 1: # for the second term of the sequence
#         return 1
#     fibo = fib(n - 1) + fib(n - 2)
#     return f"{"Message:" the {n}th term for the fibonacci series is {fibo}}
    

#     return {
#         "message": "Query successful",
#         "number": num,
#         "is_triagular": is_triangular
#     }
       


