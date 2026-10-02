---
title: "My `Helix` Setup and Config"
date: 2026-10-02
draft: false
tags: [helix, editor]
series: [Helix]        # Series classification (optional, posts in the same series show previous/next navigation)
cover: "cover.webp"
math: false                  # Set to true to enable KaTeX math formulas in this post
toc: true                    # Show table of contents
description: "My Current Helix Setup and Config"  # Used for card summary
---

## Intro
So, my Helix setup is quite simple, I learned that there are not too many things required for a good and efficient developer workflow.
The main things I need are, editing the keybinds, having a theme that would not overwhelm my eyes if I sit and write code for 5 hours straight, formatting, LSP and an efficient way to find things in my project's files. Fortunetly Helix does have all of that pretty much out of the box.

So let's get started with the config I have and other useful options that the Helix configuration provides, which you might find useful.

## Body

Okay, so let's get started. Once we [install](https://docs.helix-editor.com/package-managers.html) Helix, we can use its alias `hx` to start the program. It would look a bit basic, so we can start customising it a bit.

I guess we should first find where the config for Helix is exactly. On Mac and Linux it would be in `~/.config/helix/config.toml`, for Windows it is at: `%AppData%\helix\config.toml`. At first, most likely the file will be empty or completely missing, so we can create the directory and the file if necessary.

### Once we have the config available, we can select a [theme](https://docs.helix-editor.com/themes.html). For the theme we can press the `:` while in `NORMAL` mode and we will enter the `COMMAND` mode where we can write the `theme` command and Helix will automatically pull all the themes that are avaialable by default. I am currently using `ayu_dark`as a default theme, which means that we can just add to our config: 

```toml
theme = "ayu_dark" # Or whichever theme you liked most, you can also create your custom ones (link above)
```

### After this, we get to the [editor](https://docs.helix-editor.com/editor.html) block, this allows us to customise look and feel of the text editor. While there are a ton of options here, I think that the most important ones are: `relative line numbers`, `auto-complete`, `cursorline` for highlighting and `completion-timeout` set to 5, which is basically instantly showing completions after typing a word. My `editor` block looks like this:

```toml
[editor]
line-number = "relative"   # Relative lines
color-modes = true         # Color changes of different modes (INSERT, NORMAL, etc)
true-color = true          # Overwrite detetion of terminal true color
auto-completion = true     # Auto complete
continue-comments = false  # Comment continuation disabled, basically if we have a comment and press `Enter` the next line will start with the comment token as well
cursorline = true          # Cursor line highlighting
completion-timeout = 5     # Instant completion suggestions showing once a word is written
```

### We then have the [cursor-shape](https://docs.helix-editor.com/editor.html#editorcursor-shape-section) block which allows us to customise the look of our cursor. Here we have somewhat limited options, but still enough I would say. I am using the following setup:

```toml
[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"  
```

### Then we move to the [indent-guides](https://docs.helix-editor.com/editor.html#editorindent-guides-section) I just use `render`, which allows us to see a symbol rendered on an indented line:

```toml
[editor.indent-guides]
render = true
```

The symbol can also be configured if needed, I just use the default pipe.


### Now we move to the [soft-wrapping](https://docs.helix-editor.com/editor.html#editorsoft-wrap-section), this allows for a long line to be nicely wrapper on a new line if it would go out of the screen's bounds. I just enable it here.

```toml
[editor.soft-wrap]
enable = true
```

![helix line wrapping](../../assets/images/helix_line_wrapping.png)

We can see the symbol on the left of the second line. It is all basically 1 line, but Helix manages to wrap it up for us. I would say it is acquired taste, as not all people would like it, but it is good to know that it is there as an option.

**Important**! Do note that the soft-wrapping can conflict a bit with the `relative line numbers`, as a wrapped line DOESN'T count as one line. This means that if I have one line wrapped and shown on 3 lines, if I press `2 + k`, it moves two lines up, still on the wrapped line.


### This is a bit specific as it is all about personal preference, but we got to the [key-bindings](https://docs.helix-editor.com/remapping.html). The keymaps I use are the below ones.

```toml
[keys.normal]
S-left = "jump_view_left"              # Shift and Left arrow to move to the left split screen
S-right = "jump_view_right"            # Shift and Right arrow to move to the right split screen
S-down = "jump_view_down"              # Shift and Down arrow to move to the bottom split screen
S-up = "jump_view_up"                  # Shift and Up arrow to move to the top split screen
C-S-r = ":sh python3 %{buffer_name}"   # Control + Shift + r to run the currently opened/buffered Python file
C-S-g = ":sh go run %{buffer_name}"    # Control + Shift + g to run the currently opened/buffered Go file
C-S-z = ":sh zig run %{buffer_name}"   # Control + Shift + z to run the currently opened/buffered Zig file
"A-w" = ":wa!"                         # Alt + w to save and close all buffers
"A-q" = ":q!"                          # Alt + q to only close all buffers
")" = "@vt<space>"                     # ) character to mark and go to the next possible empty space on the line
```

You can use those as a base and extend, change them as you see fit. All other key-binds, at least in my mind were making sense, so I never had to re-bind them.

### Line [diagnostics](https://docs.helix-editor.com/editor.html#editorinline-diagnostics-section), used to render diagnostics inside the text editor

```toml
[editor.inline-diagnostics]
cursor-line = "hint"  
```
![helix line diagnostics](../../assets/images/line_diagnostics.png)

### We can continue with the [file-picker](https://docs.helix-editor.com/editor.html#editorfile-picker-section). It is maybe one of the most important things to configure, as I had some trouble with it. After a bit of debugging those are the options that work best for me:
```toml

[editor.file-picker]
hidden = false      # Do not ignore hidden files
ignore = true       # Read .ignore files
git-ignore = true   # Read .gitignore files as well
```

### The next one in the list is the [statusline](https://docs.helix-editor.com/editor.html#editorstatusline-section) that basically configures what we would see at the bottom of the editor. I currently use:

```toml
[editor.statusline]
left = ["mode", "spinner"]
center = ["file-name"]
right = ["diagnostics", "selections", "position", "file-encoding", "file-line-ending", "file-type", "file-modification-indicator", ]
separator = "|"
mode.normal = "NORMAL"
mode.insert = "INSERT"
mode.select = "SELECT"
diagnostics = ["warning", "error", "info"]
workspace-diagnostics = ["warning", "error", "info"]
```

![helix line diagnostics](../../assets/images/helix_status_line.png)

### And the last one is a bit specific, it allows us to open the file picker in the current working directory.

```toml
[keys.normal.space]
f = "file_picker_in_current_directory"
```

### Full config

```toml
theme = "ayu_dark"

[editor]
line-number = "relative"
color-modes = true
true-color = true
auto-completion = true
continue-comments = false
cursorline = true
completion-timeout = 5

[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"

[editor.indent-guides]
render = true

[editor.soft-wrap]
enable = true

[keys.normal]
S-left = "jump_view_left"
S-right = "jump_view_right"
S-down = "jump_view_down"
S-up = "jump_view_up"
C-S-r = ":sh python3 %{buffer_name}"
C-S-g = ":sh go run %{buffer_name}"
C-S-z = ":sh zig run %{buffer_name}"
"A-w" = ":wa!"
"A-q" = ":q!"
")" = "@vt<space>"

[editor.inline-diagnostics]
cursor-line = "hint"

[editor.file-picker]
hidden = false
ignore = true
git-ignore = true

[editor.statusline]
left = ["mode", "spinner"]
center = ["file-name"]
right = ["diagnostics", "selections", "position", "file-encoding", "file-line-ending", "file-type", "file-modification-indicator", ]
separator = "|"
mode.normal = "NORMAL"
mode.insert = "INSERT"
mode.select = "SELECT"
diagnostics = ["warning", "error", "info"]
workspace-diagnostics = ["warning", "error", "info"]

[keys.normal.space]
f = "file_picker_in_current_directory"  
```

## Conclusion
While Helix might seem limited in terms of customisations compared to other editors, that is not entirely the case. If you wish to put the time and effort into it, you can make Helix completely your own! If I find anything useful that I am working with daily related to the config, I will make sure to update it in the post

Stay tuned for more.
