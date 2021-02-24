# first-personal-work
采集腾讯视频《在一起》的全部评论信息
我们要对该网页的request请求进行分析，这种网页是异步加载的，Fn+F12和Fn+F5查找规律并或得数据
发现规律之后就开始使用正则爬取，将爬取到的数据保存到comments.json文件中
使用jieba第三方库对句子做精确的分词处理,用字典数据类型临时存储，统计数量
结合js插件echarts.js和echarts-wordcloud.min.js完成index.html
