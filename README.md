# lumpy

> Rips text from Lumerit course slides

### Setup

```
Download & install [Scrapy](https://doc.scrapy.org/en/latest/intro/install.html)
```

### Run

1. Add the URL of the 'overview' page of the slides to the "start_urls" array in /spiders/slideripper.py (ex. https://media.pearsoncmg.com/pls/products/coco/statistics/1256888370/presentations/ge_stat_06_overview.html)
2. Run the following command
```
$ scrapy crawl slideripper
```
3. The output will be saved to 'output.txt'

## License

MIT © [](https://twitter.com/deadsl0th)
