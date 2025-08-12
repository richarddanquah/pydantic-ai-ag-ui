"""Human in the Loop Feature.

This module implements a human-in-the-loop workflow for task planning and execution.
It uses Pydantic AI and AG-UI to create an interactive agent that suggests task steps and
requires human approval before proceeding.

No special handling is required for this feature.
"""

from __future__ import annotations

from textwrap import dedent

from pydantic_ai import Agent
from dotenv import load_dotenv
import logfire
import os


# Configure Logfire
logfire.configure(token='pylf_v1_eu_2HDRXrc65lsv3WSpq8zk6Zc8dtCt48vNv96W9f5ZqTX4')
logfire.instrument_pydantic_ai()

# Load environment variables
load_dotenv()

# Initialize the agent with enhanced instructions and Logfire instrumentation
with logfire.span("initialize_agent"):
    agent = Agent(
    'openai:gpt-4o-mini',
    instructions=dedent(
        """
        When planning tasks use tools only, without any other messages.
        IMPORTANT:
        - Use the `generate_task_steps` tool to display the suggested steps to the user
        - Never repeat the plan, or send a message detailing steps
        - If accepted, confirm the creation of the plan and the number of selected (enabled) steps only
        - If not accepted, ask the user for more information, DO NOT use the `generate_task_steps` tool again
        """
    ),
)
    
logfire.info("Agent initialized", 
              model=os.getenv('MODEL_NAME', 'openai:gpt-4o-mini'))

app = agent.to_ag_ui()
logfire.info("AG-UI interface created")
