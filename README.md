# Snail 项目简介
> Snail 是展示和分析房价的项目，数据来源：[链家网](http://sh.lianjia.com/)

## 项目架构
Snail/spiders : 爬虫脚本
####
### 解析规则
| 描述|属性| 对应的选择器|
| :--|:---|:---------|
|房屋户型 |housing_units | #introduction div.base ul li:first-child|
|建筑面积 | area | #introduction div.base ul li:nth-child(3) |
|梯户比例 | proportion | #introduction div.base ul li:nth-child(5) |
|所在楼层 | level | #introduction div.base ul li:nth-child(2)|
|房屋朝向 | direction| #introduction div.base ul li:nth-child(4) |
|装修情况 | decoration| #introduction div.base ul li:nth-child(6)|
|上次交易 | last_transaction| #introduction div.transaction ul li:nth-child(1)|
|房本年限 | age_limit | #introduction div.transaction ul li:nth-child(3)|
|房屋类型 | type | #introduction div.transaction ul li:nth-child(2) |
|是否惟一 | only | #introduction div.transaction ul li:nth-child(4) |
|地址 | address | table.aroundInfo tr:nth-child(6)|
|年代 | decade | table.aroundInfo tr:nth-child(2) td:nth-child(2)|
|首付 | first_payment | table.aroundInfo tr:nth-child(4) td:first-child|
|月供 | monthly_supply |table.aroundInfo tr:nth-child(4) td:nth-child(2)|
|单价 | unit_price| table.aroundInfo tr:first-child|
|小区 |community | table.aroundInfo tr:nth-child(5)|
|房源编号 | id| table.aroundInfo tr:nth-child(7) td:nth-child(1)|
|总价 | price| div.content div.houseInfo div.price div.mainInfo.bold|
|url | url ||

## 环境配置
> 该项目是基于Python 3.5

* 安装Python解释器
* 安装pip
* 安装scrapy模块
* 安装Flask模块

```shell
pip install scrapy
```
* 安装pyQuery模块

```shell
pip install pyQuery
```

### 启动爬虫
打开命令行，切换到项目根目录下，执行以下命令：

```shell
scrapy crawl second_hand_house
```
> second_hand_house为爬虫的名称，与`Snail/spiders`目录下定义的类`name`属性相对应，后续有可能更改

## 相关资源
* [mongodb 官方文档](https://docs.mongodb.com/)
* [Scrapy 官方教程](https://doc.scrapy.org/en/latest/intro/tutorial.html)
* [PyMongodb 教程](https://docs.mongodb.com/getting-started/python/introduction/)
* [Flask 快速入门](http://docs.jinkan.org/docs/flask/quickstart.html)
* [Flask 教程](http://flask.pocoo.org/docs/0.11/tutorial/schema/)
