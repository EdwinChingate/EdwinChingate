# Maintaining this site

The public site is a Jekyll project published by GitHub Pages from `main` at <https://edwinchingate.github.io/EdwinChingate/>. The existing `README.md` remains the GitHub profile README. The website homepage is `index.md`.

## Add an article or note

1. Copy `content_templates/article.md` into one of `_writing/`, `_stories/`, `_research/`, `_projects/`, or `_notes/`. Create the folder if it does not yet exist. Use a short lowercase filename such as `why-graphs-matter.md`.
2. Replace the title, description, date, tags, and body. The description appears in section listings and page metadata. Use a real publication date in `YYYY-MM-DD` format. Leave unpublished work on a branch until it is ready.
3. Add links with Jekyll's `relative_url` filter: `[About]({{ '/about/' | relative_url }})`. This keeps links correct under the `/EdwinChingate` project path. Link to an article with its final route, such as `[My article]({{ '/writing/my-article/' | relative_url }})`.
4. Open a pull request and check the site build. After merging to `main`, GitHub Pages will publish it at `/EdwinChingate/<section>/<filename>/`.

Each collection has an index page that lists its published Markdown entries automatically. The section pages are `writing/index.md`, `stories/index.md`, `research/index.md`, `projects/index.md`, and `notes/index.md`. Edit their introductions there. Project repository cards are maintained in `_data/projects.yml`.

## Add a standalone page or navigation item

Create `new-section/index.md` with front matter like this:

```yaml
---
title: New section
description: A short, accurate page description.
nav_key: new-section
---
```

Write its content underneath in Markdown. Add one item to `_data/navigation.yml` with matching `key`, a short `title`, and `url: /new-section/`. The shared header and active navigation state update automatically. To make it a collection with automatic article listings, add a collection to `_config.yml` and use `layout: section` in its index page.

## Change colors and layout

Edit the variables at the top of `assets/css/site.css`. `--bg` is the default background, `--surface` is the card background, `--text` is body text, `--muted` is secondary text, and `--accent` is links and highlights. Keep strong contrast, especially between body text and backgrounds. Narrow-screen rules are at the bottom of the same file. Shared page HTML is in `_layouts/` and `_includes/`; content pages do not need copied headers or footers.

## Build and verify

The site uses the `github-pages` gem so local Jekyll matches GitHub Pages. With Ruby and Bundler installed:

```sh
bundle install
bundle exec jekyll build --baseurl /EdwinChingate
python3 scripts/check_site.py _site /EdwinChingate
bundle exec jekyll serve --baseurl /EdwinChingate
```

Visit `http://127.0.0.1:4000/EdwinChingate/` for the local preview. The pull request workflow runs the same build and internal-link check. GitHub Pages continues to publish from the `main` branch root; no service or repository change is needed.
