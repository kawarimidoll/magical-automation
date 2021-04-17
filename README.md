# Magical automation

[ITエンジニアがときめく自動化の魔法 〜仕事を効率化したくなる自動化テクニック〜 Amazon](https://www.amazon.co.jp/dp/4802612486)

# python project

ref: [dockerで簡易にpython3の環境を作ってみる - Qiita](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

### build and run
```sh
docker compose up -d --build
```

### connect to the container
```sh
docker compose exec python3 bash
```

### install libraries

```sh
# in python3 container
python -m pip install scrapy
# confirm scrapy installed
scrapy version
```
