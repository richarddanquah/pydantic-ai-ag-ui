"""Example usage of the AG-UI adapter for Pydantic AI.

This provides a FastAPI application that demonstrates how to use the
Pydantic AI agent with the AG-UI protocol. It includes examples for
each of the AG-UI features:
- Human in the Loop
- Predictive State Updates
- Shared State
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os



from .api import (
    human_in_the_loop_app,
    predictive_state_updates_app,
    shared_state_app,
)


app = FastAPI(title='Pydantic AI AG-UI server')

# CORS for Next.js dev and other origins
frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin, "http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"] ,
)

app.mount('/human_in_the_loop', human_in_the_loop_app, 'Human in the Loop')
app.mount('/predictive_state_updates', predictive_state_updates_app, 'Predictive State Updates')
app.mount('/shared_state', shared_state_app, 'Shared State')

def main():
    """Main function to start the FastAPI server."""
    port = int(os.getenv("PORT", "9000"))
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()

__all__ = ["main"]
