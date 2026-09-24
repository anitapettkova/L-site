# Why I Use `Helix` and Why You Should Try It Too

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
So I started my journey with python a few years back, and naturally I was using PyCharm as a text editor, after all it was the natural choice (**PY**thon / **PY**charm get it?).
The issue is that the more I started coding and wanting to be more efficient, I no longer liked pycharm, it was bulky and dare I say even bloated, it takes care of so many things for you, which made me feel like I was not learning enough, how to setup my virtual environment, how to install my dependencies, etc.

### My First Attempts at Neovim
I watched a few youtubers using their terminal-based editors (Tsoding and his emacs was especially inspiring, though I never dared touch this artifact), so I went ahead and installed Neovim.
I am not going to lie, at first it was very hard, trying to remember all the key combinations, switching between normal and insert modes, so I decided to stick to pycharm.
Then I got hired at a new place as my first DevOps job and I wanted to be fancy, not like every other person at work who used VS Code, Pycharm or some other mainstream text editor.
So I decided that I should solder through.
### Giving Neovim a Second Chance
I installed NeoVim anew, setup the most basic plugins along with my trusty python LSP -> [ty](http://docs.astral.sh/ty/features/language-server/) and started working on my internship project. I wrote all the 1500 lines of code using only NeoVim and the project actually turned out great, as far as I know, it is still being used in the company to this day.
That all sounds great, and it was for quite some time, but I started to want more, I wanted my NeoVim to look better, to feel better, to have more features, so I started adding new plugins.
Plugin after plugin my neovim config became a bloated mess, 500+ lines of plugin definitions using [mason](https://github.com/mason-org/mason.nvim). **It was hell**, I could no longer edit anything in my editor's config, the smallest change was breaking the whole config, I tried to split it into separate modules, but it felt impossible, small changes causing Neovim to not open or if it by any coincidence opens, it was completely unusable.
### When Neovim Became the Problem
This is when I decided to look elsewhere, I needed an editor that would allow me have most of the things that Neovim provided, but I would not be married to its config.
It had to be simple, fast and most of the features I needed had to come out of the box. And voilà, I stumbled upon an article about a new editor that was gaining traction called `Helix` and I got instantly hooked.
I started reading the docs and it sounded like something I would use as my daily editor. I downloaded it and started testing. It had almost everything I needed out of the box, I could search for files, I could look for substrings in files, the keybindings were all making sense in my mind and one of the most important things, I had `Command Palette` with access to all the commands and keybindings, so if I forgot something, I could easily quickly check what its keybind was.

### Small (for me) Drawbacks of Helix

#### The Approach
Of course Helix is not the cure to everything, switching from NeoVim's action first to helix's selection first approach is hard to get used to if you are experienced nvim user.

- **You want to delete the next word?**

You press `d + w` and you get a character deleted and the rest highlited (oh how many times I did that until I get used to it).

- **You want to delete the below N lines?**

You can't just press `d + 4 + j`, you need to first mark the lines and then delete them (`4 + x + d`)

This is the main thing with Helix, you mark first then perform action on the marked target text. It can suck for experienced neovim users at first, but after a while you get used to it (I know I did). And for new users it is actually a lot more intuitive than having to learn the vim motions.

##### Customisations
- Is Helix Customisable?
That is the question, right? Well, yes, but not compared to Neovim and Emacs, `Helix` comes with a ton of features included in its default setup, mostly anything a new user would need, but you are a bit limited in terms of customisations and the lack of a plugin system does not help. Still, there are some options where you can extend the capabilities of the editor like:
  - A lot of builtin functions like: `:insert-output`, which can allow to use CLI applications like internal plugins, a great example of this is the Yazi [integration](https://github.com/sxyazi/yazi/pull/2461) in Helix that sxyazi created (and this approach can work with my other CLIs).
  - I will not get into a lot of details about this, as it is not released yet, but the plugin system at least for now looks great, it can be tested freely from Mattew Paras' repository on the [steel-event-system](https://github.com/mattwparas/helix/tree/steel-event-system) branch.
  - We also have a ton of other options for customisations provided by `Helix` itself, which can be found [here](https://docs.helix-editor.com/configuration.html)

#### Things You Get With Helix Out of the Box
While `Helix` has a lot of default features that come to mind, some of the main ones that you might be of interest to a new user are:
  - `Command Palette` including all the commands, keybinds and functions that are available - `leader + ?`
  - `File Picker` out of the box, something other editors don't have - `lead + f`
  - `Global Grep-like Search` supports regular expressions btw - `leader + /`
  - `Yanking to clipboard` - `leader + space + y`
  - `Changed File Picker` - `leader + g`
  - `Simple Window Splitting` - `ctrl + w + v` (vertical split) or `ctrl + w + s` (horizontal split)

And many more such cool features all coming out of the box!

## Conclusion
So should you switch to Helix like I did? Well, it depends entirely on your preference, if you want fine-grained control over everything in the editor, Helix might not be for you.
But if you want a good balance between customisation options, speed and out of the box features, or you just want to try a new editor, I can whole-hearthedly suggest testing Helix!

P.S I will soon create another post related to my helix config, features I mainly use, custom-keybindinds and many more. Stay tuned!