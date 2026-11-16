---
layout: section
title: Projects
nav_key: projects
kicker: Open software
description: Public scientific software projects by Edwin Chingate.
---
These public repositories connect scientific questions to computational tools. For background on the approach, see [About]({{ '/about/' | relative_url }}) and [Research]({{ '/research/' | relative_url }}).

<div class="project-grid">
{% for project in site.data.projects %}
  <article class="project-card">
    <h2><a href="{{ project.url }}">{{ project.name }} <span aria-hidden="true">↗</span></a></h2>
    <p>{{ project.description }}</p>
  </article>
{% endfor %}
</div>

## Project writeups

Longer Markdown writeups will appear below as they are published.
