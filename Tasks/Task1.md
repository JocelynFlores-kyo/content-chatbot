1. Instead of “Use the website’s sitemap.xml to query all URLs”, you need to use this zendesk api: https://support.strikingly.com/api/v2/help_center/en-us/articles.json to retrieve all the en-us support articles of Strikingly support center.

注意到，原create_embeddings.py 脚本底层逻辑是默认解析 sitemap.xml 的结构（一种 XML 格式的网站地图），而 Zendesk API 返回的是 JSON 格式数据

也就是说

sitemap.xml → 返回 XML 格式的 URL 列表

Zendesk API → 返回 JSON 格式的文章元数据（标题、正文、URL等）

在create_embeddings.py中有两种模式，分别对应两种处理方式。