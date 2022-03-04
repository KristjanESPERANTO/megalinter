<!-- markdownlint-disable MD033 MD041 -->
<!-- @generated by .automation/build.py, please do not update manually -->
# sql-lint

## sql-lint documentation

- Version in MegaLinter: **0.0.19**
- Visit [Official Web Site](https://github.com/joereynolds/sql-lint#readme){target=_blank}
- See [How to configure sql-lint rules](https://sql-lint.readthedocs.io/en/latest/files/configuration.html){target=_blank}
  - If custom `.sql-config.json` config file is not found, [.sql-config.json](https://github.com/megalinter/megalinter/tree/main/TEMPLATES/.sql-config.json){target=_blank} will be used
- See [Index of problems detected by sql-lint](https://github.com/joereynolds/sql-lint#checks){target=_blank}

[![sql-lint - GitHub](https://gh-card.dev/repos/joereynolds/sql-lint.svg?fullname=)](https://github.com/joereynolds/sql-lint){target=_blank}

## Configuration in MegaLinter

- Enable sql-lint by adding `SQL_SQL_LINT` in [ENABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)
- Disable sql-lint by adding `SQL_SQL_LINT` in [DISABLE_LINTERS variable](https://megalinter.github.io/configuration/#activation-and-deactivation)

| Variable                                 | Description                                                                                                                                                                                                         | Default value                                   |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| SQL_SQL_LINT_ARGUMENTS                   | User custom arguments to add in linter CLI call<br/>Ex: `-s --foo "bar"`                                                                                                                                            |                                                 |
| SQL_SQL_LINT_FILTER_REGEX_INCLUDE        | Custom regex including filter<br/>Ex: `(src\|lib)`                                                                                                                                                                  | Include every file                              |
| SQL_SQL_LINT_FILTER_REGEX_EXCLUDE        | Custom regex excluding filter<br/>Ex: `(test\|examples)`                                                                                                                                                            | Exclude no file                                 |
| SQL_SQL_LINT_CLI_LINT_MODE               | Override default CLI lint mode<br/>- `file`: Calls the linter for each file<br/>- `list_of_files`: Call the linter with the list of files as argument<br/>- `project`: Call the linter from the root of the project | `file`                                          |
| SQL_SQL_LINT_FILE_EXTENSIONS             | Allowed file extensions. `"*"` matches any extension, `""` matches empty extension. Empty list excludes all files<br/>Ex: `[".py", ""]`                                                                             | `[".sql"]`                                      |
| SQL_SQL_LINT_FILE_NAMES_REGEX            | File name regex filters. Regular expression list for filtering files by their base names using regex full match. Empty list includes all files<br/>Ex: `["Dockerfile(-.+)?", "Jenkinsfile"]`                        | Include every file                              |
| SQL_SQL_LINT_PRE_COMMANDS                | List of bash commands to run before the linter                                                                                                                                                                      | None                                            |
| SQL_SQL_LINT_POST_COMMANDS               | List of bash commands to run after the linter                                                                                                                                                                       | None                                            |
| SQL_SQL_LINT_CONFIG_FILE                 | sql-lint configuration file name</br>Use `LINTER_DEFAULT` to let the linter find it                                                                                                                                 | `.sql-config.json`                              |
| SQL_SQL_LINT_RULES_PATH                  | Path where to find linter configuration file                                                                                                                                                                        | Workspace folder, then MegaLinter default rules |
| SQL_SQL_LINT_DISABLE_ERRORS              | Run linter but consider errors as warnings                                                                                                                                                                          | `false`                                         |
| SQL_SQL_LINT_DISABLE_ERRORS_IF_LESS_THAN | Maximum number of errors allowed                                                                                                                                                                                    | `0`                                             |

## IDE Integration

Use sql-lint in your favorite IDE to catch errors before MegaLinter !

|                                                                 <!-- -->                                                                 | IDE                         | Extension Name                                |                                 Install                                 |
|:----------------------------------------------------------------------------------------------------------------------------------------:|-----------------------------|-----------------------------------------------|:-----------------------------------------------------------------------:|
| <img src="https://github.com/megalinter/megalinter/raw/main/docs/assets/icons/vim.ico" alt="" height="32px" class="megalinter-icon"></a> | [vim](https://www.vim.org/) | [ale](https://github.com/dense-analysis/ale/) | [Visit Web Site](https://github.com/dense-analysis/ale/){target=_blank} |

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

- File extensions: `.sql`

<!-- markdownlint-disable -->
<!-- /* cSpell:disable */ -->
### How the linting is performed

- sql-lint is called one time by identified file

### Example calls

```shell
sql-lint myfile.sql
```

```shell
sql-lint --config .sql-config.json myfile.sql
```


### Help content

```shell
Usage: sql-lint [options]

Options:
  -V, --version          output the version number
  --fix [string]         The .sql string to fix
  -d, --driver <string>  The driver to use, must be one of ['mysql',
                         'postgres']
  -v, --verbose          Brings back information on the what it's linting and
                         the tokens generated
  --format <string>      The format of the output, can be one of ['simple',
                         'json'] (default: "simple")
  --host <string>        The host for the connection
  --user <string>        The user for the connection
  --password <string>    The password for the connection
  --port <string>        The port for the connection
  --config <string>      The path to the configuration file
  -h, --help             display help for command
```

### Installation on mega-linter Docker image

- NPM packages (node.js):
  - [sql-lint](https://www.npmjs.com/package/sql-lint)

### Example success log

```shell
Results of sql-lint linter (version 0.0.15)
See documentation on https://megalinter.github.io/descriptors/sql_sql_lint/
-----------------------------------------------

[SUCCESS] .automation/test/sql/sql_good_1.sql
    

```

### Example error log

```shell
Results of sql-lint linter (version 0.0.15)
See documentation on https://megalinter.github.io/descriptors/sql_sql_lint/
-----------------------------------------------

[ERROR] .automation/test/sql/sql_bad_1.sql
    .automation/test/sql/sql_bad_1.sql:1 [sql-lint: missing-where] DELETE statement missing WHERE clause.

```