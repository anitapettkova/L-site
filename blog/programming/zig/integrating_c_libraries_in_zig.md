# Integrating C Code in Your Zig Projects

# Intro
Why would someone use C in their project? After all, if you are using a more modern low level language like zig, is it necessary to use the stinky old C?
The answer might surprise you. Some of the most useful code in the world is still written in C, and the good news is that Zig is fully compatible with it.
Yes you heard me right, you can integrate most C library in your Zig application without any issues. Let's learn how to do this.


# Body

## Importing Simple C Header Files
Zig allows us to easily [import](https://ziglang.org/documentation/0.16.0/#Import-from-C-Header-File) simple header files. Our best friends here are [cImport](https://ziglang.org/documentation/0.16.0/#cImport) and [cInclude](https://ziglang.org/documentation/0.16.0/#cInclude), those two functions are all we need for this example. Here we go, we can import any C header file we have on our system, a good example is `stdlib.h` and its `abs` function:

```zig
const std = @import("std");
const Io = std.Io;
const print = std.debug.print;

const zig_test = @import("zig_test");

const c_libs = @cImport({
    @cInclude("stdio.h");
    @cInclude("stdlib.h");
});

pub fn main(_: std.process.Init) void {
    const file_name = "test_file.txt";

    const positive_integer = c_libs.abs(-15);
    print("Positive integer via C func: {d}\n", .{positive_integer});

    const file = c_libs.fopen(file_name, "w");
    defer _ = c_libs.fclose(file);
    const bytes_read = c_libs.fprintf(file, "Some text");

    print("We successfully wrote {d} bytes to {s}\n", .{ bytes_read, file_name });
}

```
Note that `@cImport` accepts an expression, so we can pass more than one C header if we want to and we can then import from the same variable. And that is all we need, we can now use any function, variable or macro from the C header files.

## More Complex Binding
Now the above example is really cool, it works great, but what if we want to statically bind our program against a complex, large C library, for example my faviourite [raylib](https://www.raylib.com/). If you are not familiar with it, it is basically a library used for game development, though it can also be used for any GUI app pretty much. (Please do note that there are already Raylib [bindings](https://github.com/raylib-zig/raylib-zig) bindings out there, but who needs those?)

For this more complex example, we need to first clone the Raylib library locally. I always prefer to do it in a local `lib` directory:
```bash
git clone https://github.com/raysan5/raylib
```

Now we have the repository locally, but how can we actually bind it to our program? Well, we first need to build Raylib to a static library, we can first look for the static `.a` file. 
```bash
find . -iname "libraylib.a"
```

As expected the static library is missing. So we can just build it, we can navigate to the `src` directory in raylib and just run `make`:
```bash
make  
```
The output here can vary, but at the end we should see:
```bash
ar rcs ../src/libraylib.a rcore.o rshapes.o rtextures.o rtext.o rglfw.o rmodels.o raudio.o
raylib static library generated (libraylib.a) in ../src!
```

Now we can check again for our static library and we should see:
```bash
find . -iname "libraylib.a"
./src/libraylib.a
```

That is perfect, we can start linking our static library in our program. We can do that in our `build.zig` file, we can remove all the default commets from it and above our `exe` definition, we can create our new module by translating the raylib header file:

```zig
const raylib = b.addTranslateC(.{
    .root_source_file = b.path("raylib/src/raylib.h"),
    .optimize = optimize,
    .target = target,
    .link_libc = true,
});
```

Great, now in our `exe` definition we can add our new module:
```bash
    const exe = b.addExecutable(.{
        .name = "zig_test",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/main.zig"),

            .target = target,
            .optimize = optimize,

            .imports = &.{
                .{ .name = "zig_test", .module = mod },
                .{ .name = "raylib", .module = raylib.createModule() }, // <--- we name our module and create it from the translated header
            },
        }),
    });
```

We are almost there, we should now add our statically compiled library right after our `exe` definition:
```bash
exe.root_module.addObjectFile(b.path("raylib/src/libraylib.a"));
```

And our last step would be to bind the OS specific system libraries, we can handle them in a conditional check, we just need to remember to import the `builtin` module as well:
```zig
const builtin = @import("builtin");

if (builtin.target.os.tag.isDarwin()) {
    exe.root_module.linkFramework("Cocoa", .{});
    exe.root_module.linkFramework("CoreFoundation", .{});
    exe.root_module.linkFramework("IOKit", .{});
    exe.root_module.linkFramework("CoreVideo", .{});
    exe.root_module.linkFramework("OpenGL", .{});
    exe.root_module.linkFramework("QuartzCore", .{});
} else {
    exe.root_module.linkSystemLibrary("GL", .{});
    exe.root_module.linkSystemLibrary("X11", .{});
    exe.root_module.linkSystemLibrary("Xrandr", .{});
    exe.root_module.linkSystemLibrary("Xinerama", .{});
    exe.root_module.linkSystemLibrary("Xi", .{});
    exe.root_module.linkSystemLibrary("Xcursor", .{});

    exe.root_module.linkSystemLibrary("m", .{});
    exe.root_module.linkSystemLibrary("pthread", .{});
    exe.root_module.linkSystemLibrary("dl", .{});
    exe.root_module.linkSystemLibrary("rt", .{});
}
```
This handles Linux and MacOS and should provide everything that `raylib` would need. This would be how the `build.zig` file should look:

```zig
const std = @import("std");
const builtin = @import("builtin");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});

    const optimize = b.standardOptimizeOption(.{});

    const mod = b.addModule("zig_test", .{
        .root_source_file = b.path("src/root.zig"),
        .optimize = optimize,
        .target = target,
    });

    const raylib = b.addTranslateC(.{
        .root_source_file = b.path("raylib/src/raylib.h"),
        .optimize = optimize,
        .target = target,
        .link_libc = true,
    });

    const exe = b.addExecutable(.{
        .name = "zig_test",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/main.zig"),

            .target = target,
            .optimize = optimize,

            .imports = &.{
                .{ .name = "zig_test", .module = mod },
                .{ .name = "raylib", .module = raylib.createModule() },
            },
        }),
    });

    exe.root_module.addObjectFile(b.path("raylib/src/libraylib.a"));

    if (builtin.target.os.tag.isDarwin()) {
        exe.root_module.linkFramework("Cocoa", .{});
        exe.root_module.linkFramework("CoreFoundation", .{});
        exe.root_module.linkFramework("IOKit", .{});
        exe.root_module.linkFramework("CoreVideo", .{});
        exe.root_module.linkFramework("OpenGL", .{});
        exe.root_module.linkFramework("QuartzCore", .{});
    } else {
        exe.root_module.linkSystemLibrary("GL", .{});
        exe.root_module.linkSystemLibrary("X11", .{});
        exe.root_module.linkSystemLibrary("Xrandr", .{});
        exe.root_module.linkSystemLibrary("Xinerama", .{});
        exe.root_module.linkSystemLibrary("Xi", .{});
        exe.root_module.linkSystemLibrary("Xcursor", .{});

        exe.root_module.linkSystemLibrary("m", .{});
        exe.root_module.linkSystemLibrary("pthread", .{});
        exe.root_module.linkSystemLibrary("dl", .{});
        exe.root_module.linkSystemLibrary("rt", .{});
    }

    b.installArtifact(exe);

    const run_step = b.step("run", "Run the app");

    const run_cmd = b.addRunArtifact(exe);
    run_step.dependOn(&run_cmd.step);

    run_cmd.step.dependOn(b.getInstallStep());

    if (b.args) |args| {
        run_cmd.addArgs(args);
    }

    const mod_tests = b.addTest(.{
        .root_module = mod,
    });

    const run_mod_tests = b.addRunArtifact(mod_tests);

    const exe_tests = b.addTest(.{
        .root_module = exe.root_module,
    });

    const run_exe_tests = b.addRunArtifact(exe_tests);

    const test_step = b.step("test", "Run tests");
    test_step.dependOn(&run_mod_tests.step);
    test_step.dependOn(&run_exe_tests.step);
}
```

And we are all set now, we can import the module in our `main.zig` and use it freely. A simple example would be:
```zig
const std = @import("std");
const Io = std.Io;
const print = std.debug.print;

const zig_test = @import("zig_test");

const raylib = @import("raylib");

pub fn main(_: std.process.Init) void {
    const width = 800;
    const height = 450;

    raylib.InitWindow(width, height, "How To Bind C Libraries");
    while (!raylib.WindowShouldClose()) {
        raylib.BeginDrawing();
        raylib.ClearBackground(raylib.GRAY);

        raylib.DrawText("Binding against raylib!", 190, 200, 20, raylib.WHITE);
        raylib.EndDrawing();
    }

    raylib.CloseWindow();
}
```

We then compile our program and run it:
```bash
zig build run -Doptimize=ReleaseSafe
```

And voilà, we have `raylib` fully bound to our program and we can use the capabilities of the library.

# Conclusion
It is great, right? While zig does not depend in any way on `libc`, zig can easily interlop with C codebases, allowing developers to implement any C library in the program. In my opinion this is one of the strongest features of the language. If you want to know more about the compatibility of the zig compiler and all its features related to C, you can read more about it [here](https://ziglang.org/documentation/0.16.0/#C).

Stay tuned for more!
