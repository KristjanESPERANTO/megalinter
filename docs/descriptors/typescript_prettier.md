<!-- markdownlint-disable MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->

<div align="center">
  <a href="https://prettier.io/" target="blank" title="Visit linter Web Site">
    <img src="https://github.com/standard/standard/raw/master/sticker.png" alt="prettier" height="150px" class="megalinter-banner">
  </a>
</div>

## prettier documentation

- Version in MegaLinter: **2.6.0**
- Visit [Official Web Site](https://prettier.io/){target=_blank}
- See [How to configure prettier rules](https://prettier.io/docs/en/configuration.html){target=_blank}
- See [How to disable prettier rules in files](https://prettier.io/docs/en/ignore.html#javascript){target=_blank}
- See [Index of problems detected by prettier](https://prettier.io/docs/en/options.html){target=_blank}

[![prettier - GitHub](https://gh-card.dev/repos/prettier/prettier.svg?fullname=)](https://github.com/prettier/prettier){target=_blank}

## Configuration in MegaLinter

- Enable prettier by adding `TYPESCRIPT_PRETTIER` in [ENABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)
- Disable prettier by adding `TYPESCRIPT_PRETTIER` in [DISABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)

- Enable **auto-fixes** by adding `TYPESCRIPT_PRETTIER` in [APPLY_FIXES variable](https://megalinter.github.io/configuration/#apply-fixes)

| Variable                                        | Description                                                                                                                                                                                                         | Default value                                   |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| TYPESCRIPT_DEFAULT_STYLE                        | For prettier to be active, TYPESCRIPT_DEFAULT_STYLE must be `prettier`                                                                                                                                              | `standard`                                      |
| TYPESCRIPT_PRETTIER_ARGUMENTS                   | User custom arguments to add in linter CLI call<br/>Ex: `-s --foo "bar"`                                                                                                                                            |                                                 |
| TYPESCRIPT_PRETTIER_FILTER_REGEX_INCLUDE        | Custom regex including filter<br/>Ex: `(src\|lib)`                                                                                                                                                                  | Include every file                              |
| TYPESCRIPT_PRETTIER_FILTER_REGEX_EXCLUDE        | Custom regex excluding filter<br/>Ex: `(test\|examples)`                                                                                                                                                            | Exclude no file                                 |
| TYPESCRIPT_PRETTIER_CLI_LINT_MODE               | Override default CLI lint mode<br/>- `file`: Calls the linter for each file<br/>- `list_of_files`: Call the linter with the list of files as argument<br/>- `project`: Call the linter from the root of the project | `list_of_files`                                 |
| TYPESCRIPT_PRETTIER_FILE_EXTENSIONS             | Allowed file extensions. `"*"` matches any extension, `""` matches empty extension. Empty list excludes all files<br/>Ex: `[".py", ""]`                                                                             | `[".ts"]`                                       |
| TYPESCRIPT_PRETTIER_FILE_NAMES_REGEX            | File name regex filters. Regular expression list for filtering files by their base names using regex full match. Empty list includes all files<br/>Ex: `["Dockerfile(-.+)?", "Jenkinsfile"]`                        | Include every file                              |
| TYPESCRIPT_PRETTIER_PRE_COMMANDS                | List of bash commands to run before the linter                                                                                                                                                                      | None                                            |
| TYPESCRIPT_PRETTIER_POST_COMMANDS               | List of bash commands to run after the linter                                                                                                                                                                       | None                                            |
| TYPESCRIPT_PRETTIER_CONFIG_FILE                 | prettier configuration file name</br>Use `LINTER_DEFAULT` to let the linter find it                                                                                                                                 | `.prettierrc.json`                              |
| TYPESCRIPT_PRETTIER_RULES_PATH                  | Path where to find linter configuration file                                                                                                                                                                        | Workspace folder, then MegaLinter default rules |
| TYPESCRIPT_PRETTIER_DISABLE_ERRORS              | Run linter but consider errors as warnings                                                                                                                                                                          | `true`                                          |
| TYPESCRIPT_PRETTIER_DISABLE_ERRORS_IF_LESS_THAN | Maximum number of errors allowed                                                                                                                                                                                    | `0`                                             |

## IDE Integration

Use prettier in your favorite IDE to catch errors before MegaLinter !

|                                                                   <!-- -->                                                                   | IDE                                                      | Extension Name                                                                                |                                                                                   Install                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------:|----------------------------------------------------------|-----------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/atom.ico" alt="" height="32px" class="megalinter-icon"></a>   | [Atom](https://atom.io/)                                 | [prettier-atom](https://github.com/prettier/prettier-atom)                                    |                                                 [Visit Web Site](https://github.com/prettier/prettier-atom){target=_blank}                                                  |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/atom.ico" alt="" height="32px" class="megalinter-icon"></a>   | [Atom](https://atom.io/)                                 | [atom-mprettier](https://github.com/t9md/atom-mprettier)                                      |                                                   [Visit Web Site](https://github.com/t9md/atom-mprettier){target=_blank}                                                   |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/atom.ico" alt="" height="32px" class="megalinter-icon"></a>   | [Atom](https://atom.io/)                                 | [atom-miniprettier](https://github.com/duailibe/atom-miniprettier)                            |                                               [Visit Web Site](https://github.com/duailibe/atom-miniprettier){target=_blank}                                                |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/emacs.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Emacs](https://www.gnu.org/software/emacs/)             | [prettier-emacs](https://github.com/prettier/prettier-emacs)                                  |                                                 [Visit Web Site](https://github.com/prettier/prettier-emacs){target=_blank}                                                 |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/emacs.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Emacs](https://www.gnu.org/software/emacs/)             | [prettier.el](https://github.com/jscheid/prettier.el)                                         |                                                   [Visit Web Site](https://github.com/jscheid/prettier.el){target=_blank}                                                   |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/emacs.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Emacs](https://www.gnu.org/software/emacs/)             | [apheleia](https://github.com/raxod502/apheleia)                                              |                                                    [Visit Web Site](https://github.com/raxod502/apheleia){target=_blank}                                                    |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/idea.ico" alt="" height="32px" class="megalinter-icon"></a>   | [IDEA](https://www.jetbrains.com/products.html#type=ide) | [native support](https://prettier.io/docs/en/webstorm.html)                                   |                                                 [Visit Web Site](https://prettier.io/docs/en/webstorm.html){target=_blank}                                                  |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/sublime.ico" alt="" height="32px" class="megalinter-icon"></a> | [Sublime Text](https://www.sublimetext.com/)             | [JsPrettier](https://packagecontrol.io/packages/JsPrettier)                                   |                                               [Visit Web Site](https://packagecontrol.io/packages/JsPrettier){target=_blank}                                                |
|   <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/vim.ico" alt="" height="32px" class="megalinter-icon"></a>   | [vim](https://www.vim.org/)                              | [vim-prettier](https://github.com/prettier/vim-prettier)                                      |                                                  [Visit Web Site](https://github.com/prettier/vim-prettier){target=_blank}                                                  |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/default.ico" alt="" height="32px" class="megalinter-icon"></a> | visual_studio                                            | [JavaScriptPrettier](https://github.com/madskristensen/JavaScriptPrettier)                    |                                            [Visit Web Site](https://github.com/madskristensen/JavaScriptPrettier){target=_blank}                                            |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/vscode.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Visual Studio Code](https://code.visualstudio.com/)     | [prettier-vscode](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) | [![Install in VsCode](https://github.com/megalinter/megalinter/raw/main/docs/assets/images/btn_install_vscode.png)](vscode:extension/esbenp.prettier-vscode){target=_blank} |

## MegaLinter Flavours

This linter is available in the following flavours

|                                                                         <!-- -->                                                                         | Flavor                                                         | Description                                           | Embedded linters |                                                                                                                                                                                           Info |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------|:------------------------------------------------------|:----------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/images/mega-linter-square.png" alt="" height="32px" class="megalinter-icon"></a> | [all](https://megalinter.github.io/supported-linters/)         | Default MegaLinter Flavor                             |        97        |                       ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter) |
|     <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/javascript.ico" alt="" height="32px" class="megalinter-icon"></a>      | [javascript](https://megalinter.github.io/flavors/javascript/) | Optimized for JAVASCRIPT or TYPESCRIPT based projects |        50        | ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-javascript/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-javascript) |

## Behind the scenes

### How are identified applicable files

- File extensions: `.ts`

<!-- markdownlint-disable -->
<!-- /* cSpell:disable */ -->
### How the linting is performed

- prettier is called once with the list of files as arguments

### Example calls

```shell
prettier --check myfile.ts
```

```shell
prettier --config .prettierrc.json --check myfile.ts
```

```shell
prettier --config .prettierrc.json --write myfile.ts
```


### Help content

```shell
Usage: prettier [options] [file/dir/glob ...]

By default, output is written to stdout.
Stdin is read if it is piped to Prettier and no files are given.

Output options:

  -c, --check              Check if the given files are formatted, print a human-friendly summary
                           message and paths to unformatted files (see also --list-different).
  -l, --list-different     Print the names of files that are different from Prettier's formatting (see also --check).
  -w, --write              Edit files in-place. (Beware!)

Format options:

  --arrow-parens <always|avoid>
                           Include parentheses around a sole arrow function parameter.
                           Defaults to always.
  --bracket-same-line      Put > of opening tags on the last line instead of on a new line.
                           Defaults to false.
  --no-bracket-spacing     Do not print spaces between brackets.
  --embedded-language-formatting <auto|off>
                           Control how Prettier formats quoted code embedded in the file.
                           Defaults to auto.
  --end-of-line <lf|crlf|cr|auto>
                           Which end of line characters to apply.
                           Defaults to lf.
  --html-whitespace-sensitivity <css|strict|ignore>
                           How to handle whitespaces in HTML.
                           Defaults to css.
  --jsx-single-quote       Use single quotes in JSX.
                           Defaults to false.
  --parser <flow|babel|babel-flow|babel-ts|typescript|acorn|espree|meriyah|css|less|scss|json|json5|json-stringify|graphql|markdown|mdx|vue|yaml|glimmer|html|angular|lwc>
                           Which parser to use.
  --print-width <int>      The line length where Prettier will try wrap.
                           Defaults to 80.
  --prose-wrap <always|never|preserve>
                           How to wrap prose.
                           Defaults to preserve.
  --quote-props <as-needed|consistent|preserve>
                           Change when properties in objects are quoted.
                           Defaults to as-needed.
  --no-semi                Do not print semicolons, except at the beginning of lines which may need them.
  --single-attribute-per-line
                           Enforce single attribute per line in HTML, Vue and JSX.
                           Defaults to false.
  --single-quote           Use single quotes instead of double quotes.
                           Defaults to false.
  --tab-width <int>        Number of spaces per indentation level.
                           Defaults to 2.
  --trailing-comma <es5|none|all>
                           Print trailing commas wherever possible when multi-line.
                           Defaults to es5.
  --use-tabs               Indent with tabs instead of spaces.
                           Defaults to false.
  --vue-indent-script-and-style
                           Indent script and style tags in Vue files.
                           Defaults to false.

Config options:

  --config <path>          Path to a Prettier configuration file (.prettierrc, package.json, prettier.config.js).
  --no-config              Do not look for a configuration file.
  --config-precedence <cli-override|file-override|prefer-file>
                           Define in which order config files and CLI options should be evaluated.
                           Defaults to cli-override.
  --no-editorconfig        Don't take .editorconfig into account when parsing configuration.
  --find-config-path <path>
                           Find and print the path to a configuration file for the given input file.
  --ignore-path <path>     Path to a file with patterns describing files to ignore.
                           Defaults to .prettierignore.
  --plugin <path>          Add a plugin. Multiple plugins can be passed as separate `--plugin`s.
                           Defaults to [].
  --plugin-search-dir <path>
                           Custom directory that contains prettier plugins in node_modules subdirectory.
                           Overrides default behavior when plugins are searched relatively to the location of Prettier.
                           Multiple values are accepted.
                           Defaults to [].
  --with-node-modules      Process files inside 'node_modules' directory.

Editor options:

  --cursor-offset <int>    Print (to stderr) where a cursor at the given position would move to after formatting.
                           This option cannot be used with --range-start and --range-end.
                           Defaults to -1.
  --range-end <int>        Format code ending at a given character offset (exclusive).
                           The range will extend forwards to the end of the selected statement.
                           This option cannot be used with --cursor-offset.
                           Defaults to Infinity.
  --range-start <int>      Format code starting at a given character offset.
                           The range will extend backwards to the start of the first line containing the selected statement.
                           This option cannot be used with --cursor-offset.
                           Defaults to 0.

Other options:

  --no-color               Do not colorize error messages.
  --no-error-on-unmatched-pattern
                           Prevent errors when pattern is unmatched.
  --file-info <path>       Extract the following info (as JSON) for a given file path. Reported fields:
                           * ignored (boolean) - true if file path is filtered by --ignore-path
                           * inferredParser (string | null) - name of parser inferred from file path
  -h, --help <flag>        Show CLI usage, or details about the given flag.
                           Example: --help write
  -u, --ignore-unknown     Ignore unknown files.
  --insert-pragma          Insert @format pragma into file's first docblock comment.
                           Defaults to false.
  --loglevel <silent|error|warn|log|debug>
                           What level of logs to report.
                           Defaults to log.
  --no-plugin-search       Disable plugin autoloading.
  --require-pragma         Require either '@prettier' or '@format' to be present in the file's first docblock comment
                           in order for it to be formatted.
                           Defaults to false.
  --stdin-filepath <path>  Path to the file to pretend that stdin comes from.
  --support-info           Print support information as JSON.
  -v, --version            Print Prettier version.


```

### Installation on mega-linter Docker image

- NPM packages (node.js):
  - [typescript](https://www.npmjs.com/package/typescript)
  - [prettier](https://www.npmjs.com/package/prettier)