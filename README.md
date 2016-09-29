# Snail 项目简介
> Snail 是展示和分析房价的项目，数据来源：[链家网](http://sh.lianjia.com/)

## 项目架构
Snail/spiders : 爬虫脚本

## 环境配置
> 该项目是基于Python 3.5

* 安装Python解释器
* 安装pip
* 安装scrapy模块

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
scrapy crawl quotes
```