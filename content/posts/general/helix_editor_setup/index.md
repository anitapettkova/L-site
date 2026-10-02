---
title: "Why I Use Helix and Why You Should Try It Too"
date: 2026-10-01
draft: false
tags: [helix, editor]
series: [Helix]        # Series classification (optional, posts in the same series show previous/next navigation)
cover: "cover.webp"
math: false                  # Set to true to enable KaTeX math formulas in this post
toc: true                    # Show table of contents
description: "Why you need to try Helix as a text editor"  # Used for card summary
---

What is Helix? And why does it exist when we already have Neovim, Emacs, VS Code, and countless other editors?

I asked myself the same question before making the switch. In this article, I’ll share my journey from PyCharm to Neovim and eventually to Helix, why I left each editor behind, and what made Helix stick as my daily editor.

## Why Helix?
- Less configuration, more time spent coding.
- Powerful features such as LSP, file picking, and global search are built in.
- Fast, keyboard-driven, and designed to run in the terminal.
- Selection-first editing provides a different and more intuitive editing workflow.
- Fewer plugins mean less configuration and maintenance.
- The trade-off is less customisation compared with Neovim or Emacs.

## From PyCharm to Neovim
I started my journey with Python a few years back, and naturally, I was using PyCharm as my text editor. After all, it was the natural choice (PYthon / PYcharm, get it?).

The issue was that the more I started coding and looking for ways to become more efficient, the less I liked PyCharm. It was bulky and, dare I say, even bloated. It took care of so many things for me that I started feeling like I wasn't learning enough about what was actually happening under the hood: how to set up my virtual environment, how to install my dependencies, etc.

### My First Attempts at Neovim
I watched a few YouTubers using their terminal-based editors (Tsoding and his Emacs were especially inspiring, though I never dared to touch this artifact), so I went ahead and installed Neovim.

I'm not going to lie: at first, it was very hard. Trying to remember all the key combinations and constantly switching between normal and insert modes was overwhelming, so I decided to stick with PyCharm.

Then I got hired at a new place for my first DevOps job, and I wanted to be fancy. I didn't want to be like everyone else at work using VS Code, PyCharm, or some other mainstream text editor.

So I decided to soldier through.

### Giving Neovim a Second Chance
I installed Neovim again, set up the most basic plugins along with my trusty Python LSP, [ty](http://docs.astral.sh/ty/features/language-server/), and started working on my internship project.

I wrote all 1,500 lines of code using only Neovim, and the project actually turned out great. As far as I know, it is still being used by the company to this day.

### When Neovim Became the Problem
That all sounds great, and it was for quite some time. But eventually, I started wanting more. I wanted my Neovim to look better, feel better, and have more features, so I started adding plugins.

Plugin after plugin, my Neovim config became a bloated mess: 500+ lines of plugin definitions using [Mason](https://github.com/mason-org/mason.nvim).

**It was hell.**

I could no longer comfortably edit anything in my editor's config. The smallest change would break the whole thing. I tried splitting it into separate modules, but it felt impossible. Small changes would cause Neovim to either not open at all or, if it did open, be completely unusable.

### Discovering Helix
This is when I decided to look elsewhere. I needed an editor that would give me most of what Neovim provided, without making me feel married to its configuration.

It had to be simple, fast, and have most of the features I needed built in.

And voilà, I stumbled upon an article about a new editor that was gaining traction called `Helix`, and I was instantly hooked.

I started reading the docs, and it sounded like something I could actually use as my daily editor. I downloaded it and started testing.

It had almost everything I needed out of the box. I could search for files, look for substrings across files, and the keybindings actually made sense to me. And, perhaps most importantly, I had the `Command Palette`, with access to all the available commands and keybindings. If I forgot how to do something, I could simply look it up instead of having to remember everything.

## What Helix Does Differently

### Selection-First Editing
Of course, Helix is not the cure for everything. Switching from Neovim's action-first approach to Helix's selection-first approach can be difficult to get used to, especially if you're already an experienced Neovim user.

- **You want to delete the next word?**

You press `d + w` and get a character deleted while the rest is highlighted. (Oh, how many times I did that before I got used to it.)

- **You want to delete the below N lines?**

You can't just press `d + 4 + j`, you need to first mark the lines and then delete them (`4 + x + d`).

This is the main thing with Helix: you mark the target text first and then perform the action on it. It can be frustrating for experienced Neovim users at first, but after a while, you get used to it (I know I did).

But for new users, it can actually be a lot more intuitive than having to learn Vim motions.

## The Trade-offs

### Customisations
Is Helix customisable?

That is the question, right? Well, yes, but not to the same extent as Neovim or Emacs.

`Helix` comes with a ton of features included in its default setup, pretty much everything a new user would need. However, you are more limited when it comes to customisation, and the lack of a plugin system doesn't help.

Still, there are some ways to extend the capabilities of the editor:

- A lot of builtin functions like: `:insert-output`, which can allow to use CLI applications like internal plugins, a great example of this is the Yazi [integration](https://github.com/sxyazi/yazi/pull/2461) in Helix that sxyazi created (and this approach can work with my other CLIs).
- I won't get into too much detail about this since it hasn't been released yet, but the plugin system looks promising so far. It can be tested from Matthew Paras' repository on the [steel-event-system](https://github.com/mattwparas/helix/tree/steel-event-system) branch.
- There are also plenty of other customisation options provided by `Helix itself`, which you can find in the [configuration documentation](https://docs.helix-editor.com/configuration.html).  

## What You Get Out of the Box

While `Helix` has a lot of features included by default, here are some of the main ones that might be of interest to a new user:

### Command Palette
`leader + ?` - Command Palette, including all the available commands, keybinds and functions

### File Picker
`leader + f` - File Picker out of the box, something other editors don't have

### Global Search
`leader + /` - Global Grep-like Search with support for regular expressions

### Yanking to Clipboard
`leader + space + y`

### Changed File Picker
`leader + g`

### Window Splitting
`ctrl + w + v` - Vertical split

`ctrl + w + s` - Horizontal split

And many more cool features, all coming out of the box!

## Conclusion
So, should you switch to Helix like I did? Well, it depends entirely on your preferences. If you want fine-grained control over everything in your editor, Helix might not be for you.

But if you want a good balance between customisation options, speed, and out-of-the-box features, or you just want to try a new editor, I can wholeheartedly recommend giving Helix a try!

P.S. I will soon create another post about my Helix config, the features I mainly use, custom keybindings, and many more things. Stay tuned!
