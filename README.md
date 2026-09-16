*This is an informational summary of Quarto Hub. It is not the Quarto Hub source code; that lives in [quarto-dev/q2](https://github.com/quarto-dev/q2).*

# Quarto Hub

**Prose and code belong in one place. So do the people.**

Quarto Hub is a Quarto editor in the browser that renders while you type. You edit the Quarto markdown (source) or make changes directly in the rendered page, and either way it's the same `.qmd` underneath. When you want input, you share a link: teammates and agents edit and comment in your project, not in a doc or PDF someone emails back.

**Site:** https://quarto-dev.github.io/quarto-hub/ · **App:** https://public-preview.quarto-hub.com (approved accounts only during the preview)

![The Quarto Hub editor: project files on the left, .qmd source in the middle, the rendered page on the right.](images/editor.png)

## Why

Quarto's premise is that code, analysis, and writing belong in one artifact: Markdown that can reproduce results and be versioned. What has been missing is the other half: several people in the same document at once, comments where the words are, no one waiting for a render or a pull request. Hub adds that half without giving up the plain-text, code-first ethos underneath.

## What works today

- **Websites and docs.** The whole project: file tree, outline, every page rendered as you edit it.
- **Slides.** revealjs decks, edited and previewed in place. Edit together and present from a common version.
- **Meeting notes.** One `.qmd` the whole team types into during the call, rendered as the discussion happens.
- **Agents.** Point your favorite LLM at the project. It edits the same files you do, and every change stays in the history.

Anyone with a project link can open it, read it, and comment, with no account or Quarto install. You sign in to create and own projects. **quarto-hub.com is experimental and currently available by invite only.**

## Coming soon

- **Hosted code execution.** R, Python, and Julia cells currently run in the author's local Quarto 2 environment. Later releases will add remote execution, so cells run without anything installed locally.
- **Positron.** Open a Hub project in Positron and edit alongside people working in the browser.

## Built on Quarto 2

Rendering on every keystroke requires a much faster Quarto. That is [Quarto 2](https://github.com/quarto-dev/q2): the engine rewritten in Rust, more than an order of magnitude faster than Quarto 1, and small enough to run inside the browser tab. Quarto 2 is highly functional but still experimental. It is the future of Quarto; Quarto 1 (`quarto-cli`) remains supported for many years to come.

| | |
|---|---|
| **Quarto Hub** | The web editor and file hosting for collaborative `.qmd` projects. |
| **Quarto 2** | The engine. Runs natively and in the browser. Experimental today. |
| **`quarto-cli`** | Quarto 1. Still supported, still what you install today for production work. |

## This repository

The source for the landing site. Pages are authored in Quarto Hub and synced here; pushes to `main` publish to GitHub Pages via [`.github/workflows/publish.yml`](.github/workflows/publish.yml), which strips Hub-only frontmatter and review comments (`scripts/prepare-publish.py`) before rendering with quarto-cli.

To build locally: `quarto render` (or `q2 render`), then serve `_site/`. Note that `q2 preview` does not yet load custom SCSS themes, so the preview will appear unstyled.

Something broken? [File an issue](https://github.com/quarto-dev/quarto-hub/issues).
