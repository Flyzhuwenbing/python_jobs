# python_jobs
基于scrapy框架对拉勾网进行信息抓取
1.添加请求头部信息header，user-agent模拟浏览器
2.在settings中设置DOWNLOAD_DELAY = 3,解决访问过快的问题
3.由异步加载网页返回的json格式数据设置items
4.采用mongodb进行数据存储

以拉勾为例，采用ECharts进行数据展示

https://htmlpreview.github.io/?https://github.com/Flyzhuwenbing/python_jobs/blob/master/wordcloud.html



