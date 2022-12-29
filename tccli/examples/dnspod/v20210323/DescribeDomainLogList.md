**Example 1: 获取域名日志**

 

Input: 

```
tccli dnspod DescribeDomainLogList --cli-unfold-argument  \
    --Domain test.com \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "LogList": [
            "2021-01-18 12:06:11: (111.111.111.111) 添加 A 记录 默认 线路 ftp 值 64.144.7.51"
        ],
        "PageSize": 100,
        "TotalCount": 1
    }
}
```

