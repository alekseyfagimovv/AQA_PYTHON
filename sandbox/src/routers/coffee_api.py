# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel
# from typing import Optional

# app = FastAPI(title="КиноЛавка Bug Tracker")

# # --- In-memory storage ---
# bugs: dict[int, dict] = {}
# _next_id = 1

# # --- Допустимые переходы жизненного цикла бага ---
# ALLOWED_TRANSITIONS: dict[str, set[str]] = {
#     "New":            {"Assigned"},
#     "Assigned":       {"In Progress", "Reopened"},
#     "In Progress":    {"Fixed", "Reopened"},
#     "Fixed":          {"Ready for QA", "Reopened"},
#     "Ready for QA":   {"Verified", "Reopened"},
#     "Verified":       {"Closed", "Reopened"},
#     "Closed":         {"Reopened"},
#     "Reopened":       {"Assigned", "In Progress"},
# }

# ALL_STATUSES = set(ALLOWED_TRANSITIONS.keys())


# # --- Schemas ---
# class BugCreate(BaseModel):
#     title: str
#     severity: str           # Critical | Major | Minor | Trivial
#     priority: str           # High | Medium | Low


# class BugTransition(BaseModel):
#     to_status: str


# # --- Endpoints ---
# @app.post("/bugs", status_code=status.HTTP_201_CREATED)
# def create_bug(payload: BugCreate):
#     global _next_id
#     bug_id = _next_id
#     _next_id += 1
#     bugs[bug_id] = {
#         "id": bug_id,
#         "title": payload.title,
#         "severity": payload.severity,
#         "priority": payload.priority,
#         "status": "New",
#     }
#     return bugs[bug_id]


# @app.get("/bugs/{bug_id}")
# def get_bug(bug_id: int):
#     if bug_id not in bugs:
#         raise HTTPException(status_code=404, detail="Bug not found")
#     return bugs[bug_id]


# @app.post("/bugs/{bug_id}/transition")
# def transition_bug(bug_id: int, payload: BugTransition):
#     if bug_id not in bugs:
#         raise HTTPException(status_code=404, detail="Bug not found")

#     bug = bugs[bug_id]
#     current = bug["status"]
#     target = payload.to_status

#     if target not in ALL_STATUSES:
#         raise HTTPException(status_code=400, detail=f"Unknown status: {target}")

#     if target not in ALLOWED_TRANSITIONS[current]:
#         raise HTTPException(
#             status_code=409,
#             detail=f"Illegal transition: {current} -> {target}",
#         )

#     # Бизнес-правило: при Reopened priority автоматически становится High
#     if target == "Reopened":
#         bug["priority"] = "High"

#     bug["status"] = target
#     return bug


# @app.delete("/bugs/{bug_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_bug(bug_id: int):
#     if bug_id not in bugs:
#         raise HTTPException(status_code=404, detail="Bug not found")
#     del bugs[bug_id]



# class TaskRepo:
#     def __init__(self):
#         self._store = {}
#         self._next_id = 1

#     def add(self, title: str) -> int:
#         task_id = self._next_id
#         self._store[task_id] = {"id": task_id, "title": title, "done": False}
#         self._next_id += 1
#         return task_id

#     def get(self, task_id: int) -> dict | None:
#         return self._store.get(task_id)

#     def mark_done(self, task_id: int) -> bool:
#         if task_id in self._store:
#             self._store[task_id]["done"] = True
#             return True
#         return False




# coffee_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from itertools import count

app = FastAPI(title="Coffee Shop Demo")

# --- фейковая БД ---
_orders: dict[int, dict] = {}
_id_seq = count(start=1)

# --- схемы ---
class OrderRequest(BaseModel):
    quantity: int

class OrderResponse(BaseModel):
    id: int
    status: str
    quantity: int
    message: str

# --- эндпоинты ---
@app.post("/coffee/order", response_model=OrderResponse, status_code=201)
async def create_order(order: OrderRequest):
    if not (1 <= order.quantity <= 10):
        raise HTTPException(status_code=400, detail="quantity must be between 1 and 10")

    order_id = next(_id_seq)
    record = {
        "id": order_id,
        "status": "created",
        "quantity": order.quantity,
        "message": f"Принято {order.quantity} чашек кофе",
    }
    _orders[order_id] = record
    return record

@app.get("/coffee/order/{order_id}", response_model=OrderResponse)
async def get_order(order_id: int):
    record = _orders.get(order_id)
    if record is None:
        raise HTTPException(status_code=404, detail="order not found")
    return record

@app.delete("/coffee/order/{order_id}", status_code=204)
async def delete_order(order_id: int):
    if order_id not in _orders:
        raise HTTPException(status_code=404, detail="order not found")
    del _orders[order_id]
    return None