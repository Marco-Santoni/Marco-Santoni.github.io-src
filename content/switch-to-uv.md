Title: Switch to UV
Date: 2025-10-20

I just moved the git repo of this blog from an old conda+pip based setup to using `uv`. On Mac, start by

```bash
brew install uv
```

Then, I initialized the uv project and just imported the dependencies specified in the `requirements.txt` file.

```bash
uv init --python 3.13
uv add --requirements requirements.txt
```

And that is basically it. From now on, to run pelican commands, just prefix them with `uv run`, e.g.,

```bash
uv run pelican content
```

The transition was smooth and fast. Highly recommended!