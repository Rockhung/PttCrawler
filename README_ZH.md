#ReadMe

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. 複製config_example.ini

```bash
cp config_example.ini config.ini
```

2. ini設定

```ini
[Database]
# Database Url: [Type]://[Name]
# 目前只支援SQLite
Type = sqlite
Name = ptt.db

[PttUser]
# term.ptt.cc 每個動作的間隔
Delaytime = 0.8
# selenium 需要用到的webdriver的資料夾
WebdriverFolder = webdriver
# term.ptt.cc 的 登入帳號密碼
UserId = guest
UserPwd = guest
# Choices = {database, json, both}
Output = both

[PttArticle]
# Delaytime 是每篇文章之間的Delaytime
# NextPageDelaytime 是WebPtt索引頁之間的Delaytime
Delaytime = 1.0
NextPageDelaytime = 10.0
Timeout = 10
# Choices = {database, json, both}
Output = both
```

## Usage

### Crawler

1. PTT 文章爬蟲

    從WebPtt爬取文章

    ```bash
    python -m crawler article (--start-date | --index START_INDEX END_INDEX) [--config-path CONFIG_PATH]
    ```

2. PTT 鄉民上站紀錄爬蟲

    利用term.ptt.cc爬取上站紀錄、登入次數、有效文章

    ```bash
    python -m crawler user (--database | --ip IP) [--config-path CONFIG_PATH]
    ```

3. PTT 查Ip Autonomous System Number

    查Ip的ASN(主要查Country code)

    ```bash
    python -m crawler asn (--database | --id ID) [--config-path CONFIG_PATH]
    ```

### Export

匯出成ods或csv

```bash
python export.py --format {ods, csv} --output-folder OUTPUT_FOLDER [--output-prefix OUTPUT_PREFIX]
```

### Schedule

將crawler加入系統排程

1. Update

```bash
python schedule.py update {article, asn, user} -c CYCLE_TIME [-s START_DATETIME]
```

2. Remove

```bash
python schedule.py remove {article, asn, user}
```

## 檔案結構

```text
PttCrawler/
|- utils.py
|- export.py
|- query.py
|- schedule.py
|- config_example.ini
|- models/
|   |- __init__.py
|   |- base.py
|   |- article.py
|   |- asn.py
|   `- user.py
|- crawler/
|   |- __init__.py
|   |- article.py
|   |- asn.py
|   |- user.py
|- webdriver/
|   |- windows/
|   |   `- chromedriver.exe
|   |- linux/
|   |   `- chromedriver
|   `- mac/
|       `- chromedriver
|- requirements.txt
|- CHANGELOG.md
|- README.md
`- README_ZH.md

```