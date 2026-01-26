# RagaliQ - Project Context

## What is this project?

RagaliQ (RAG + Quality) is a Python library + CLI tool for automated testing of RAG (Retrieval-Augmented Generation) pipelines. It enables QA and AI engineers to write quality tests for LLM responses using pytest-like syntax.

## Tech Stack

- Python 3.14+
- Pydantic v2 for data validation
- Anthropic SDK (Claude as LLM-as-Judge)
- Typer for CLI
- Rich for terminal output
- Pytest plugin architecture

## Project Structure

```
src/ragaliq/
├── core/           # TestCase, Evaluator base, Runner
├── evaluators/     # Faithfulness, Relevance, Hallucination, etc.
├── judges/         # LLM judge implementations (Claude, OpenAI)
├── datasets/       # Test data loading and generation
├── reports/        # Console, HTML, JSON reporters
├── integrations/   # Pytest plugin, CI helpers
└── cli/            # Typer CLI commands
```

## Key Design Decisions

1. **Evaluator Pattern**: Each metric (faithfulness, relevance, etc.) is a separate Evaluator class with `evaluate()` method
2. **LLM-as-Judge**: We use Claude API to assess response quality, not hardcoded rules
3. **Async-first**: All LLM calls are async for performance
4. **Pydantic everywhere**: Strict typing with Pydantic models for all data structures
5. **Pytest-native**: Library should feel natural to pytest users

## Code Style

- Use `ruff` for linting and formatting
- Type hints required for all public functions
- Docstrings in Google style
- Tests in `tests/` mirroring `src/` structure

## Current Phase

Phase 1: Foundation - building core models and Claude judge integration.

## Important Files

- `docs/PROJECT_PLAN.md` - Full implementation plan with weekly milestones
- `docs/ARCHITECTURE.md` - Detailed component specifications

## Commands

```bash
# Development
make install        # Install in dev mode
make test          # Run tests
make lint          # Run ruff
make format        # Format code

# CLI (after install)
ragaliq run tests.json
ragaliq generate ./docs/ -n 50
```
