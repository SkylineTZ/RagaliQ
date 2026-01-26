# Getting Started with Claude Code

## Setup

1. **Copy the project to your local machine:**
   ```bash
   # Create directory and copy files (or clone from GitHub once you set it up)
   mkdir ragaliq
   cd ragaliq
   # Copy the files from this session
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install in development mode:**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Verify setup:**
   ```bash
   make test
   ```

## Working with Claude Code

### Initial Setup

When you first open the project in Claude Code:

```bash
cd /path/to/ragaliq
claude
```

Claude Code will automatically read `CLAUDE.md` for project context.

### Recommended Prompts for Each Phase

#### Phase 1, Week 1 (completed):
- [x] Project structure
- [x] Core models (RAGTestCase, RAGTestResult, EvaluationResult)
- [x] Base Evaluator class
- [x] Initial tests

#### Phase 1, Week 2 - Claude Judge Integration:

```
Let's implement the Claude judge. Start with:
1. Create src/ragaliq/judges/base.py with abstract LLMJudge class
2. Create src/ragaliq/judges/claude.py implementing ClaudeJudge
3. Add prompt templates in src/ragaliq/judges/prompts/

The judge should have methods:
- extract_claims(response: str) -> list[str]
- verify_claim(claim: str, context: list[str]) -> bool
- score_relevance(query: str, response: str) -> float

Use async methods and tenacity for retry logic.
```

#### Phase 2, Week 3 - Core Evaluators:

```
Now implement the core evaluators. Start with FaithfulnessEvaluator:
1. Create src/ragaliq/evaluators/faithfulness.py
2. It should extract claims from response, then verify each against context
3. Score = verified_claims / total_claims
4. Add unit tests with mocked judge

Follow the same pattern for RelevanceEvaluator and HallucinationEvaluator.
```

### Tips for Effective Claude Code Sessions

1. **Be specific about what you want:**
   - Bad: "Implement the evaluators"
   - Good: "Implement FaithfulnessEvaluator in src/ragaliq/evaluators/faithfulness.py following the pattern in docs/PROJECT_PLAN.md"

2. **Reference existing files:**
   - "Follow the same pattern as test_case.py"
   - "Use the EvaluationResult model from core/evaluator.py"

3. **Ask for tests together with code:**
   - "Implement X and add unit tests in tests/unit/test_X.py"

4. **Iterate in small chunks:**
   - Don't ask for the entire project at once
   - One module at a time with tests

5. **Run tests frequently:**
   ```bash
   make test-fast  # Quick test run
   make lint       # Check code style
   ```

## Next Steps Checklist

### Week 2: Claude Judge
- [ ] `src/ragaliq/judges/base.py` - Abstract LLMJudge
- [ ] `src/ragaliq/judges/claude.py` - ClaudeJudge implementation
- [ ] `src/ragaliq/judges/prompts/extract_claims.yaml`
- [ ] `src/ragaliq/judges/prompts/verify_claim.yaml`
- [ ] `tests/unit/test_judges.py`

### Week 3: Core Evaluators
- [ ] `src/ragaliq/evaluators/faithfulness.py`
- [ ] `src/ragaliq/evaluators/relevance.py`
- [ ] `src/ragaliq/evaluators/hallucination.py`
- [ ] `tests/unit/test_evaluators.py`

### Week 4: RAG Evaluators
- [ ] `src/ragaliq/evaluators/context_precision.py`
- [ ] `src/ragaliq/evaluators/context_recall.py`
- [ ] Evaluator registry

## Environment Variables

Create `.env` file (not committed):
```
ANTHROPIC_API_KEY=your-key-here
OPENAI_API_KEY=your-key-here  # optional
```

## Common Commands

```bash
# Development
make install-dev    # Install with dev dependencies
make test           # Run all tests
make test-fast      # Run tests without coverage
make lint           # Check code style
make format         # Auto-format code
make typecheck      # Run mypy

# After project is complete
make build          # Build package
make publish-test   # Publish to TestPyPI
```
