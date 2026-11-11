from fastapi import FastAPI

app = FastAPI(
title="Business tools API",
description="This is a simple API for business tools.",
version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to business tools API"}


@app.get("/calculate")
def calculate(price: float, quantity: int):
    total = price * quantity
    return {"total": total, "price": price, "quantity": quantity}


@app.post("/discount")
def apply_discount(price: float, discount: float):
    discounted_price = price - (price * (discount / 100))
    return {"original_price": price, "discount": discount, "discounted_price": discounted_price}



