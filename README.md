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
