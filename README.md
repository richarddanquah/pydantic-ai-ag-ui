# Pydantic AI AG-UI

This directory contains example usage of the AG-UI adapter for Pydantic AI. It provides a FastAPI application that demonstrates how to use the Pydantic AI agent with the AG-UI protocol.

## Features

The examples include implementations for each of the AG-UI features:
- Human in the Loop


## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Export OPENAI_API_KEY:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```
3. Run the development server:
   ```bash
   uv run dev
   ```

## Usage

Once the server is running, launch the frontend with:
https://github.com/ag-ui-protocol/ag-ui/tree/main/typescript-sdk

```bash
cd ../../../
pnpm install
turbo run dev
```

and view it at http://localhost:3000.

By default, the agents can be reached at:

- `http://localhost:9000/human_in_the_loop` - Human in the Loop


<img width="1037" height="625" alt="Screenshot 2025-08-12 at 22 52 14" src="https://github.com/user-attachments/assets/37b26f71-e6ef-4eb4-910d-ad4ce0c3cc87" />
<img width="1143" height="715" alt="Screenshot 2025-08-12 at 22 52 04" src="https://github.com/user-attachments/assets/44a1c5da-29d4-4583-9778-b6b8c3f84bd1" />

<img width="978" height="618" alt="Screenshot 2025-08-12 at 22 52 31" src="https://github.com/user-attachments/assets/09c41f65-e06a-425a-800f-32d03b36b8b7" />



## Tutorial
https://www.youtube.com/watch?v=fhF1qSyg9j4