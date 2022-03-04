<!-- markdownlint-disable MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->

<div align="center">
  <a href="https://stylelint.io" target="blank" title="Visit linter Web Site">
    <img src="https://github.com/stylelint/stylelint/raw/master/identity/stylelint-icon-and-text-white.png" alt="stylelint" height="150px" class="megalinter-banner">
  </a>
</div>

## stylelint documentation

- Version in MegaLinter: **14.5.3**
- Visit [Official Web Site](https://stylelint.io){target=_blank}
- See [How to configure stylelint rules](https://stylelint.io/user-guide/configure){target=_blank}
  - If custom `.stylelintrc.json` config file is not found, [.stylelintrc.json](https://github.com/megalinter/megalinter/tree/main/TEMPLATES/.stylelintrc.json){target=_blank} will be used
- See [How to disable stylelint rules in files](https://stylelint.io/user-guide/ignore-code){target=_blank}
- See [Index of problems detected by stylelint](https://stylelint.io/user-guide/rules/list){target=_blank}

[![stylelint - GitHub](https://gh-card.dev/repos/stylelint/stylelint.svg?fullname=)](https://github.com/stylelint/stylelint){target=_blank}

## Configuration in MegaLinter

- Enable stylelint by adding `CSS_STYLELINT` in [ENABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)
- Disable stylelint by adding `CSS_STYLELINT` in [DISABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)

- Enable **auto-fixes** by adding `CSS_STYLELINT` in [APPLY_FIXES variable](https://megalinter.github.io/configuration/#apply-fixes)

| Variable                                  | Description                                                                                                                                                                                                         | Default value                                   |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| CSS_STYLELINT_ARGUMENTS                   | User custom arguments to add in linter CLI call<br/>Ex: `-s --foo "bar"`                                                                                                                                            |                                                 |
| CSS_STYLELINT_FILTER_REGEX_INCLUDE        | Custom regex including filter<br/>Ex: `(src\|lib)`                                                                                                                                                                  | Include every file                              |
| CSS_STYLELINT_FILTER_REGEX_EXCLUDE        | Custom regex excluding filter<br/>Ex: `(test\|examples)`                                                                                                                                                            | Exclude no file                                 |
| CSS_STYLELINT_CLI_LINT_MODE               | Override default CLI lint mode<br/>- `file`: Calls the linter for each file<br/>- `list_of_files`: Call the linter with the list of files as argument<br/>- `project`: Call the linter from the root of the project | `list_of_files`                                 |
| CSS_STYLELINT_FILE_EXTENSIONS             | Allowed file extensions. `"*"` matches any extension, `""` matches empty extension. Empty list excludes all files<br/>Ex: `[".py", ""]`                                                                             | `[".css", ".scss", ".saas"]`                    |
| CSS_STYLELINT_FILE_NAMES_REGEX            | File name regex filters. Regular expression list for filtering files by their base names using regex full match. Empty list includes all files<br/>Ex: `["Dockerfile(-.+)?", "Jenkinsfile"]`                        | Include every file                              |
| CSS_STYLELINT_PRE_COMMANDS                | List of bash commands to run before the linter                                                                                                                                                                      | None                                            |
| CSS_STYLELINT_POST_COMMANDS               | List of bash commands to run after the linter                                                                                                                                                                       | None                                            |
| CSS_STYLELINT_CONFIG_FILE                 | stylelint configuration file name</br>Use `LINTER_DEFAULT` to let the linter find it                                                                                                                                | `.stylelintrc.json`                             |
| CSS_STYLELINT_RULES_PATH                  | Path where to find linter configuration file                                                                                                                                                                        | Workspace folder, then MegaLinter default rules |
| CSS_STYLELINT_DISABLE_ERRORS              | Run linter but consider errors as warnings                                                                                                                                                                          | `false`                                         |
| CSS_STYLELINT_DISABLE_ERRORS_IF_LESS_THAN | Maximum number of errors allowed                                                                                                                                                                                    | `0`                                             |

## IDE Integration

Use stylelint in your favorite IDE to catch errors before MegaLinter !

|                                                                   <!-- -->                                                                   | IDE                                                  | Extension Name                                                                                     |                                                                                     Install                                                                                     |
|:--------------------------------------------------------------------------------------------------------------------------------------------:|------------------------------------------------------|----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/atom.ico" alt="" height="32px" class="megalinter-icon"></a>   | [Atom](https://atom.io/)                             | [linter-stylelint](https://github.com/AtomLinter/linter-stylelint)                                 |                                                 [Visit Web Site](https://github.com/AtomLinter/linter-stylelint){target=_blank}                                                 |
|  <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/emacs.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Emacs](https://www.gnu.org/software/emacs/)         | [flycheck](https://github.com/flycheck/flycheck)                                                   |                                                      [Visit Web Site](https://github.com/flycheck/flycheck){target=_blank}                                                      |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/sublime.ico" alt="" height="32px" class="megalinter-icon"></a> | [Sublime Text](https://www.sublimetext.com/)         | [SublimeLinter-stylelint](https://github.com/SublimeLinter/SublimeLinter-stylelint)                |                                            [Visit Web Site](https://github.com/SublimeLinter/SublimeLinter-stylelint){target=_blank}                                            |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/sublime.ico" alt="" height="32px" class="megalinter-icon"></a> | [Sublime Text](https://www.sublimetext.com/)         | [SublimeLinter-contrib-stylelint_d](https://github.com/jo-sm/SublimeLinter-contrib-stylelint_d)    |                                           [Visit Web Site](https://github.com/jo-sm/SublimeLinter-contrib-stylelint_d){target=_blank}                                           |
|   <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/vim.ico" alt="" height="32px" class="megalinter-icon"></a>   | [vim](https://www.vim.org/)                          | [ale](https://github.com/dense-analysis/ale)                                                       |                                                     [Visit Web Site](https://github.com/dense-analysis/ale){target=_blank}                                                      |
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/vscode.ico" alt="" height="32px" class="megalinter-icon"></a>  | [Visual Studio Code](https://code.visualstudio.com/) | [vscode-stylelint](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint) | [![Install in VsCode](https://github.com/megalinter/megalinter/raw/main/docs/assets/images/btn_install_vscode.png)](vscode:extension/stylelint.vscode-stylelint){target=_blank} |

## MegaLinter Flavours

This linter is available in the following flavours

|                                                                         <!-- -->                                                                         | Flavor                                                               | Description                                           | Embedded linters |                                                                                                                                                                                                 Info |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------|:------------------------------------------------------|:----------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/images/mega-linter-square.png" alt="" height="32px" class="megalinter-icon"></a> | [all](https://megalinter.github.io/supported-linters/)               | Default MegaLinter Flavor                             |        97        |                             ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/dart.ico" alt="" height="32px" class="megalinter-icon"></a>         | [dart](https://megalinter.github.io/flavors/dart/)                   | Optimized for DART based projects                     |        41        |                   ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-dart/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-dart) |
|    <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/documentation.ico" alt="" height="32px" class="megalinter-icon"></a>    | [documentation](https://megalinter.github.io/flavors/documentation/) | MegaLinter for documentation projects                 |        40        | ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-documentation/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-documentation) |
|       <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/dotnet.ico" alt="" height="32px" class="megalinter-icon"></a>        | [dotnet](https://megalinter.github.io/flavors/dotnet/)               | Optimized for C, C++, C# or VB based projects         |        47        |               ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-dotnet/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-dotnet) |
|         <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/go.ico" alt="" height="32px" class="megalinter-icon"></a>          | [go](https://megalinter.github.io/flavors/go/)                       | Optimized for GO based projects                       |        42        |                       ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-go/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-go) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/java.ico" alt="" height="32px" class="megalinter-icon"></a>         | [java](https://megalinter.github.io/flavors/java/)                   | Optimized for JAVA based projects                     |        42        |                   ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-java/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-java) |
|     <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/javascript.ico" alt="" height="32px" class="megalinter-icon"></a>      | [javascript](https://megalinter.github.io/flavors/javascript/)       | Optimized for JAVASCRIPT or TYPESCRIPT based projects |        49        |       ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-javascript/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-javascript) |
|         <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/php.ico" alt="" height="32px" class="megalinter-icon"></a>         | [php](https://megalinter.github.io/flavors/php/)                     | Optimized for PHP based projects                      |        45        |                     ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-php/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-php) |
|       <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/python.ico" alt="" height="32px" class="megalinter-icon"></a>        | [python](https://megalinter.github.io/flavors/python/)               | Optimized for PYTHON based projects                   |        49        |               ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-python/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-python) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/ruby.ico" alt="" height="32px" class="megalinter-icon"></a>         | [ruby](https://megalinter.github.io/flavors/ruby/)                   | Optimized for RUBY based projects                     |        41        |                   ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-ruby/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-ruby) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/rust.ico" alt="" height="32px" class="megalinter-icon"></a>         | [rust](https://megalinter.github.io/flavors/rust/)                   | Optimized for RUST based projects                     |        41        |                   ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-rust/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-rust) |
|     <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/salesforce.ico" alt="" height="32px" class="megalinter-icon"></a>      | [salesforce](https://megalinter.github.io/flavors/salesforce/)       | Optimized for Salesforce based projects               |        43        |       ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-salesforce/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-salesforce) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/scala.ico" alt="" height="32px" class="megalinter-icon"></a>        | [scala](https://megalinter.github.io/flavors/scala/)                 | Optimized for SCALA based projects                    |        41        |                 ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-scala/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-scala) |
|        <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/swift.ico" alt="" height="32px" class="megalinter-icon"></a>        | [swift](https://megalinter.github.io/flavors/swift/)                 | Optimized for SWIFT based projects                    |        41        |                 ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-swift/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-swift) |
|      <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/terraform.ico" alt="" height="32px" class="megalinter-icon"></a>      | [terraform](https://megalinter.github.io/flavors/terraform/)         | Optimized for TERRAFORM based projects                |        46        |         ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/megalinter/megalinter-terraform/v5) ![Docker Pulls](https://img.shields.io/docker/pulls/megalinter/megalinter-terraform) |

## Behind the scenes

### How are identified applicable files

- File extensions: `.css`, `.scss`, `.saas`

<!-- markdownlint-disable -->
<!-- /* cSpell:disable */ -->
### How the linting is performed

- stylelint is called once with the list of files as arguments

### Example calls

```shell
stylelint myfile.css
```

```shell
stylelint --config .stylelintrc.json myfile.css myfile2.css myfile3.css
```

```shell
stylelint --fix --config .stylelintrc.json myfile.css myfile2.css myfile3.css
```


### Help content

```shell

  A mighty, modern CSS linter.

  Usage: stylelint [input] [options]

  Input: Files(s), glob(s), or nothing to use stdin.

    If an input argument is wrapped in quotation marks, it will be passed to
    globby for cross-platform glob support. node_modules are always ignored.
    You can also pass no input and use stdin, instead.

  Options:

    --config

      Path to a specific configuration file (JSON, YAML, or CommonJS), or the
      name of a module in node_modules that points to one. If no --config
      argument is provided, stylelint will search for configuration files in
      the following places, in this order:
        - a stylelint property in package.json
        - a .stylelintrc file (with or without filename extension:
          .json, .yaml, .yml, and .js are available)
        - a stylelint.config.js file exporting a JS object
      The search will begin in the working directory and move up the directory
      tree until a configuration file is found.

    --config-basedir

      An absolute path to the directory that relative paths defining "extends"
      and "plugins" are *relative to*. Only necessary if these values are
      relative paths.

    --print-config

      Print the configuration for the given path.

    --ignore-path, -i

      Path to a file containing patterns that describe files to ignore. The
      path can be absolute or relative to process.cwd(). By default, stylelint
      looks for .stylelintignore in process.cwd().

    --ignore-pattern, --ip

      Pattern of files to ignore (in addition to those in .stylelintignore)

    --fix

      Automatically fix problems of certain rules.

    --custom-syntax

      Module name or path to a JS file exporting a PostCSS-compatible syntax.

    --stdin

      Accept stdin input even if it is empty.

    --stdin-filename

      A filename to assign stdin input.

    --ignore-disables, --id

      Ignore stylelint-disable comments.

    --disable-default-ignores, --di

      Allow linting of node_modules.

    --cache                       [default: false]

      Store the info about processed files in order to only operate on the
      changed ones the next time you run stylelint. By default, the cache
      is stored in "./.stylelintcache". To adjust this, use --cache-location.

    --cache-location              [default: '.stylelintcache']

      Path to a file or directory to be used for the cache location.
      Default is "./.stylelintcache". If a directory is specified, a cache
      file will be created inside the specified folder, with a name derived
      from a hash of the current working directory.

      If the directory for the cache does not exist, make sure you add a trailing "/"
      on *nix systems or "\" on Windows. Otherwise the path will be assumed to be a file.

    --formatter, -f               [default: "string"]

      The output formatter: "compact", "json", "string", "tap", "unix" or "verbose".

    --custom-formatter

      Path to a JS file exporting a custom formatting function.

    --quiet, -q

      Only register problems for rules with an "error"-level severity (ignore
      "warning"-level).

    --color
    --no-color

      Force enabling/disabling of color.

    --report-needless-disables, --rd

      Also report errors for stylelint-disable comments that are not blocking a lint warning.
      The process will exit with code 2 if needless disables are found.

    --report-invalid-scope-disables, --risd

      Report stylelint-disable comments that used for rules that don't exist within the configuration object.
      The process will exit with code 2 if invalid scope disables are found.

    --report-descriptionless-disables, --rdd

      Report stylelint-disable comments without a description.
      The process will exit with code 2 if descriptionless disables are found.

    --max-warnings, --mw

      Number of warnings above which the process will exit with code 2.
      Useful when setting "defaultSeverity" to "warning" and expecting the
      process to fail on warnings (e.g. CI build).

    --output-file, -o

      Path of file to write report.

    --version, -v

      Show the currently installed version of stylelint.

    --allow-empty-input, --aei

      When glob pattern matches no files, the process will exit without throwing an error.

```

### Installation on mega-linter Docker image

- NPM packages (node.js):
  - [stylelint](https://www.npmjs.com/package/stylelint)
  - [stylelint-config-standard](https://www.npmjs.com/package/stylelint-config-standard)
  - [stylelint-config-sass-guidelines](https://www.npmjs.com/package/stylelint-config-sass-guidelines)
  - [stylelint-scss](https://www.npmjs.com/package/stylelint-scss)

### Example success log

```shell
Results of stylelint linter (version 13.8.0)
See documentation on https://megalinter.github.io/descriptors/css_stylelint/
-----------------------------------------------

[SUCCESS] .automation/test/css/css_good_01.css
    

```

### Example error log

```shell
Results of stylelint linter (version 13.8.0)
See documentation on https://megalinter.github.io/descriptors/css_stylelint/
-----------------------------------------------

[ERROR] .automation/test/css/css_bad_01.css
    
    .automation/test/css/css_bad_01.css
     2:1   ✖  Expected empty line before comment   comment-empty-line-before
     3:1   ✖  Expected empty line before comment   comment-empty-line-before
     5:5   ✖  Expected indentation of 2 spaces     indentation              
     5:33  ✖  Expected "#FFFFFF" to be "#ffffff"   color-hex-case           
     5:33  ✖  Expected "#FFFFFF" to be "#FFF"      color-hex-length         
     6:5   ✖  Expected indentation of 2 spaces     indentation              
     7:5   ✖  Expected indentation of 2 spaces     indentation              
     8:5   ✖  Expected indentation of 2 spaces     indentation              
     8:12  ✖  Expected "#AAAAAA" to be "#aaaaaa"   color-hex-case           
     8:12  ✖  Expected "#AAAAAA" to be "#AAA"      color-hex-length

```