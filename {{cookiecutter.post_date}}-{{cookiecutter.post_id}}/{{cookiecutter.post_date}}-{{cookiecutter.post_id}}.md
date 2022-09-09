---
layout: post
title:  {{cookiecutter.post_title}}
date:   {% now 'utc', '%Y-%m-%d' %}
author: {{cookiecutter.post_author}}
{%- if cookiecutter.post_tags %}
tags: {{cookiecutter.post_tags}}
{%- endif %}
{%- if cookiecutter.post_categories %}
categories: {{cookiecutter.post_categories}}
{%- endif %}
excerpt: {{cookiecutter.post_excerpt}}
---

<!-- TODO: Add your post content here. -->