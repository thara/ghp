# ghp
GitHub command line tools made with Python.

**This project is in development. It has not been released yet.**

## Usage

### Pull Request

```
ghp pull-request [subcommand] [--flags]
```
**Alias:** `ghp pr`


#### Exmaple

* List pull request in WIP sorted by updated in current Git project

    ```
$ ghp pr -l WIP -s updated
#4 DDDD @tomochikahara (4 days ago)
#3 CCCC @tomochikahara (3 days ago)
#1 BBBB @tomochikahara (2 days ago)
#1 AAAA @tomochikahara (1 days ago)
```