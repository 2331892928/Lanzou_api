# 一个取蓝奏直链的python源码
# 此源码为本人第一次接触python制作，见谅，支持一直更新，因为蓝奏直链提取的规则一直在变
# 功能：取所有蓝奏链接的直链，不止是直链
#返回示例：
- {'info': 'sucess', 't': 'https://vip.d0.baidupan.com/file/?B2FTbQk4BTQBCFNrADUFaVFuUGhU7ACZAJYG5gfVWvxXsFezD+kDsAPuUJlRKAc3VyMBflFnA3EFJFQ0VGEBbAdiU1sJPQU1AWpTNgBjBTBRMlBlVDgAMgA+BiYHPVooV2pXMQ9kA2EDZVA0UTIHIFd9AXRRMwMzBTJUYFQ5AS8HN1M2CXsFYQFjUyoANwVnUThQN1RpADEAYgY0B2Nab1dmVzQPZgNkAzBQZ1EzBzJXawE8UT4DMgVmVGtUbQE5B2RTNwkwBTIBNVNhAHoFflFiUCVULQB3AHQGZQcpWjJXM1c9D2QDYwNsUDVRMAcxVysBcFFnA2wFZ1Q0VDUBMQcxUzUJbQVkAW5TNwBkBTJRPVB7VCUAJABhBmwHLFpmV2ZXNg9jA24DZlAwUTYHPlc4ATZRKAN0BXJUJVQ1ATEHMVM1CWYFZQFnUzYAYQU9UTNQc1R+AGsAdwY9B2paY1dkVy4PYANkA2VQKFExBzRXIwE1UT8=', 'name_all': '监控系统-1.zip', 'size': '162.1 K'}
# 失败示例：
- {'info': 0}  
# 字段解释：
t：文件下载直链  
name_all: 文件全名，包括后缀  
size: 文件大小  
下边的字段，不是所有蓝奏链接都有，只有分享的链接为文件夹，才有这些字段  
icon:文件类型  
id: 蓝奏文件页面  
time: 上传时间  
duan：未知  
p_ico： 未知  
