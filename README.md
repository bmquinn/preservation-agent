# preservation-agent 🏛️

An intelligent digital preservation assistant built with 🤗 Hugging Face's `smolagents` framework. This agent specializes in analyzing IIIF manifests and image metadata to support digital preservation workflows.

## Features 🌟

- Automated analysis of IIIF manifests for preservation metadata
- Technical metadata extraction from image files
- Interactive REPL interface for preservation tasks
- Structured thought process combining reasoning and code execution
- Extensible tool system for preservation-specific functionality

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bmquinn/preservation-agent.git
cd preservation-agent
```

2. Create and activate a virtual environment using `uv`:

```bash
uv venv --python 3.10
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv sync
```

4. Install and configure the Hugging Face CLI:

```bash
pip install --upgrade huggingface-hub
huggingface-cli login
```

Visit [Hugging Face CLI installation guide](https://huggingface.co/docs/huggingface_hub/en/installation) for more details on setting up your credentials.

## Dependencies

Project dependencies are managed through `pyproject.toml`:

- smolagents >= 1.0.0
- piffle >= 0.6.0
- Python >= 3.10

## Usage

The preservation agent operates through an interactive REPL interface where you can input preservation-related queries:

```python
from preservation_agent import create_agent

uv run main.py
```

This will start the interactive REPL where you can input preservation queries:

```bash
> Analyze the IIIF manifest at https://example.org/manifest.json
```

### Example Queries

```bash
> Analyze the IIIF manifest at https://example.org/manifest.json
> What can you tell me about /Users/user/example_image.jpg?
```

## System Design

The agent uses a structured approach to solving preservation tasks:

1. **Thought Phase**: Analyzes the preservation task and plans the approach
2. **Code Phase**: Executes Python code to interact with preservation tools
3. **Observation Phase**: Processes results for the next step or final answer

## Contributing

Contributions are welcome! Areas for enhancement include:

- Additional preservation metadata extractors
- New preservation-specific tools
- Improved manifest analysis capabilities
- Extended format support

## License

MIT

## Acknowledgments

Built with the 🤗 Hugging Face `smolagents` framework - the simplest way to build powerful AI agents.
