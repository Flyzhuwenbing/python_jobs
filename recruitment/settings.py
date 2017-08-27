# -*- coding: utf-8 -*-

# Scrapy settings for recruitment project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'recruitment'

SPIDER_MODULES = ['recruitment.spiders']
NEWSPIDER_MODULE = 'recruitment.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'recruitment (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   'Accept-Encoding' : 'gzip, deflate, sdch',
   'Accept-Language' : 'zh-CN,zh;q=0.8',
   'Cache-Control' : 'max-age=0',
   'Cookie' : 'ga=GA1.2.1708517389.1499422583; _gid=GA1.2.871580085.1503142968; LastCity%5Fid=765; LastCity=%e6%b7%b1%e5%9c%b3; JSSearchModel=0; dywez=95841923.1503195733.5.3.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/searchresult.ashx; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1503142776,1503188779; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1503196618; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e9%a4%90%e8%a1%a5%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e5%8c%85%e4%bd%8f%7c%e6%88%bf%e8%a1%a5%7c%e5%8c%85%e5%90%83%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4; LastSearchHistory=%7b%22Id%22%3a%227993e483-270b-4929-8230-2d358083a6e3%22%2c%22Name%22%3a%22python+%2b+%e6%ad%a6%e6%b1%89%2b%e8%a5%bf%e5%ae%89%2b%e6%88%90%e9%83%bd%2b%e5%a4%a7%e8%bf%9e%2b%e9%95%bf%e6%98%a5%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e6%25ad%25a6%25e6%25b1%2589%3b%25e8%25a5%25bf%25e5%25ae%2589%3b%25e6%2588%2590%25e9%2583%25bd%3b%25e5%25a4%25a7%25e8%25bf%259e%3b%25e9%2595%25bf%25e6%2598%25a5%26kw%3dpython%26sm%3d0%26p%3d37%26isfilter%3d0%26isadv%3d0%26sg%3d227ef6e3b8d447d6a7293452d63ed532%22%2c%22SaveTime%22%3a%22%5c%2fDate(1503216072188%2b0800)%5c%2f%22%7d; dywea=95841923.2438924229749401000.1499422583.1503195733.1503198739.6; dywec=95841923; dyweb=95841923.18.8.1503216020267; __utma=269921210.1708517389.1499422583.1503195733.1503198740.6; __utmb=269921210.18.9.1503216022755; __utmc=269921210; __utmz=269921210.1503195733.5.3.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/searchresult.ashx',
   'Host' : 'sou.zhaopin.com',
   'Proxy-Connection' : 'keep-alive',
   'Referer' : 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89%2B%E8%A5%BF%E5%AE%89%2B%E6%88%90%E9%83%BD%2B%E5%A4%A7%E8%BF%9E%2B%E9%95%BF%E6%98%A5&kw=python&p=1&isadv=0',
   'Upgrade-Insecure-Requests': 1,
   'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'recruitment.middlewares.RecruitmentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'recruitment.middlewares.ProxyMiddleWare': 1,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
     'recruitment.pipelines.python_lg': 200,
     'recruitment.pipelines.python_zl': 300,

}
HOST = "localhost"
PORT = 27017
DB = "jobs"
COLLECTION1 = "lg"
COLLECTION2 = "zl"

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
