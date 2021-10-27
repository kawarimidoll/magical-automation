# Magical automation

[ITエンジニアがときめく自動化の魔法 〜仕事を効率化したくなる自動化テクニック〜 Amazon](https://www.amazon.co.jp/dp/4802612486)

## python project

ref: [dockerで簡易にpython3の環境を作ってみる - Qiita](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

### build and run
```sh
docker compose up -d
# needs `--build` when first run
# docker compose up -d --build
```

### connect to the container
confirm the container is running
```sh
docker compose exec python3 bash
```

## first scrapy project
### install scrapy

```sh
# in python3 container
python -m pip install scrapy
# confirm scrapy installed
scrapy version
```

### create scrapy project

```sh
scrapy startproject amazon
cd amazon
scrapy genspider amazon_spider amazon.co.jp
# created amazon/spiders/amazon_spider.py
```

## first selenium project

### install libraries

```sh
# in python3 container
python -m pip install selenium
python -m pip install chromedriver
```

### create selenium project

```sh
mkdir selenium_amazon
cd selenium_amazon
```

## scrapy crawler
create project

```sh
scrapy startproject socym
cd socym
scrapy genspider socym_spider socym.co.jp
# created socym/spiders/socym_spider.py
```

run

```sh
scrapy crawl socym_spider
```

## temperature open data

```sh
mkdir temperatures
cd temperatures
curl https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/alltable/mxtemsadext00_rct.csv > max.csv
vi max_temp.py # create script
python max_temp.py
```
