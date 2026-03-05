# Contributing to pinaxai

Pinaxai is an open-source project and we welcome contributions. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## 🎯 Getting Started

Looking for a way to contribute? Check out issues labeled [`good first issue`](https://github.com/Pinax-Labs/pinaxai/labels/good%20first%20issue) or [`help wanted`](https://github.com/Pinax-Labs/pinaxai/labels/help%20wanted) for beginner-friendly tasks.

## 👩‍💻 How to contribute

Please follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow:

1. Fork the repository.
2. Create a new branch for your feature (see [Branch Naming](#branch-naming) below).
3. Add your feature or improvement.
4. Ensure your code passes formatting and validation checks.
5. Send a pull request.
6. We appreciate your support & input!

### Branch Naming

Use a descriptive branch name with a conventional prefix:

- `feat/short-description` — for new features
- `fix/issue-123` — for bug fixes (reference the issue number when applicable)
- `docs/update-readme` — for documentation changes
- `refactor/module-name` — for code refactoring

## Reporting Issues

### Bug Reports

When reporting a bug, please include:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Python version, OS, and `pinaxai` version
- Relevant logs or error messages

### Feature Requests

For feature requests, please describe:

- The problem your feature would solve
- Your proposed solution or approach
- Any alternatives you've considered

## Development Setup

> **Requires Python 3.10 or later.** We recommend Python 3.12 for development.

1. Clone the repository.
2. Check if you have `uv` installed by running `uv --version`.
   - If you have `uv` installed, you can skip this step.
   - If you don't have `uv` installed, you can install it by running `pip install uv`.
3. Create a virtual environment:
   - For Unix, use `./scripts/dev_setup.sh`.
   - For Windows, use `.\scripts\dev_setup.bat`.
   - This setup will:
     - Create a `.venv` virtual environment in the current directory.
     - Install the required packages.
     - Install the `pinaxai` package in editable mode.
4. Activate the virtual environment:
   - On Unix: `source .venv/bin/activate`
   - On Windows: `.venv\Scripts\activate`

> From here on you have to use `uv pip install` to install missing packages

## Commit & PR Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages. Each commit message should be structured as:

```
<type>(<optional scope>): <description>
```

Common types:

| Type | Purpose |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes |
| `refactor` | Code refactoring (no functional change) |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks (CI, deps, etc.) |

**PR titles** should also follow this convention. PRs are squash-merged into `main`.

## Formatting and validation

Ensure your code meets our quality standards by running the appropriate formatting and validation script before submitting a pull request:

- For Unix:
  - `./scripts/format.sh`
  - `./scripts/validate.sh`
- For Windows:
  - `.\scripts\format.bat`
  - `.\scripts\validate.bat`

These scripts will perform code formatting with `ruff` and static type checks with `mypy`.

## Local testing

Before submitting a pull request, ensure all tests pass locally:

1. Do the development setup above.

2. Run the test suite: `./scripts/test.sh`

3. Run specific test files or test cases: `pytest ./libs/pinaxai/tests/unit/utils/test_string.py` or whatever file you want to test.

**Test organization:**

- **Unit tests** live alongside the code in `libs/pinaxai/tests/unit/`
- **Integration tests** are in `libs/pinaxai/tests/integration/`
- Tests use **pytest** as the test framework

Make sure all tests pass before submitting your pull request. If you add new features, include appropriate test coverage.

## Adding a new Vector Database

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `libs/pinaxai/pinaxai/vectordb` for the new vector database.
3. Create a Class for your VectorDb that implements the `VectorDb` interface:
   - Your Class will be in the `libs/pinaxai/pinaxai/vectordb/<your_db>/<your_db>.py` file.
   - The `VectorDb` interface is defined in `libs/pinaxai/pinaxai/vectordb/base.py`.
   - Import your `VectorDb` Class in `libs/pinaxai/pinaxai/vectordb/<your_db>/__init__.py`.
   - Checkout the [`libs/pinaxai/pinaxai/vectordb/pgvector/pgvector`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/vectordb/pgvector/pgvector.py) file for an example.
4. Add a recipe for using your `VectorDb` under `cookbook/agent_concepts/knowledge/vector_dbs/<your_db>`.
   - Checkout [`cookbook/agent_concepts/knowledge/vector_dbs/pg_vector`](https://github.com/Pinax-Labs/pinaxai/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pg_vector.py) for an example.
5. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
6. Submit a pull request.

## Adding a new Model Provider

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `libs/pinaxai/pinaxai/models` for the new Model provider.
3. If the Model provider supports the OpenAI API spec:
   - Create a Class for your LLM provider that inherits the `OpenAILike` Class from `libs/pinaxai/pinaxai/models/openai/like.py`.
   - Your Class will be in the `libs/pinaxai/pinaxai/models/<your_model>/<your_model>.py` file.
   - Import your Class in the `libs/pinaxai/pinaxai/models/<your_model>/__init__.py` file.
   - Checkout the [`pinaxai/models/together/together.py`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/models/together/together.py) file for an example.
4. If the Model provider does not support the OpenAI API spec:
   - Reach out to us on [Discord](https://discord.gg/4MtYHHrgA8) or open an issue to discuss the best way to integrate your LLM provider.
   - Checkout [`pinaxai/models/anthropic/claude.py`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/models/anthropic/claude.py) or [`pinaxai/models/cohere/chat.py`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/models/cohere/chat.py) for inspiration.
5. Add a recipe for using your Model provider under `cookbook/models/<your_model>`.
   - Checkout [`pinaxai/cookbook/models/aws/claude`](https://github.com/Pinax-Labs/pinaxai/tree/main/cookbook/models/aws/claude) for an example.
6. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
7. Submit a pull request.

## Adding a new Tool

1. Setup your local environment by following the [Development setup](#development-setup).
2. Create a new directory under `libs/pinaxai/pinaxai/tools` for the new Tool.
3. Create a Class for your Tool that inherits the `Toolkit` Class from `libs/pinaxai/pinaxai/tools/toolkit.py`.
   - Your Class will be in `libs/pinaxai/pinaxai/tools/<your_tool>.py`.
   - Make sure to register all functions in your class via a flag.
   - Checkout the [`pinaxai/tools/youtube_tools.py`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/tools/youtube_tools.py) file for an example.
   - If your tool requires an API key, checkout the [`pinaxai/tools/serpapi_tools.py`](https://github.com/Pinax-Labs/pinaxai/blob/main/libs/pinaxai/pinaxai/tools/serpapi_tools.py) as well.
4. Add a recipe for using your Tool under `cookbook/tools/<your_tool>`.
   - Checkout [`pinaxai/cookbook/tools/youtube_tools`](https://github.com/Pinax-Labs/pinaxai/blob/main/cookbook/tools/youtube_tools.py) for an example.
5. Important: Format and validate your code by running `./scripts/format.sh` and `./scripts/validate.sh`.
6. Submit a pull request.

Message us on [Discord](https://discord.gg/4MtYHHrgA8) or post on [Discourse](https://community.pinax.tech/) if you have any questions or need help with credits.

## 📚 Resources

- [Documentation](https://docs.pinax.tech/introduction)
- [Discord](https://discord.gg/4MtYHHrgA8)
- [Discourse](https://community.pinax.tech/)

## 📝 License

This project is licensed under the terms of the [MPL-2.0 license](/LICENSE). By contributing, you agree that your contributions will be licensed under the same license.
