**Example 1: 获取域名下增值服务用量**

获取域名下增值服务用量

Input: 

```
tccli dnspod DescribeVASStatistic --cli-unfold-argument  \
    --DomainId 4397543
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "VASList": [
            {
                "Name": "域名别名",
                "Key": "name",
                "LimitCount": 999,
                "UseCount": 0
            },
            {
                "Name": "负载均衡",
                "Key": "lb",
                "LimitCount": 999,
                "UseCount": 2
            },
            {
                "Name": "URL 转发",
                "Key": "url",
                "LimitCount": 9999,
                "UseCount": 0
            },
            {
                "Name": "线路分组",
                "Key": "group",
                "LimitCount": 9999,
                "UseCount": 2
            },
            {
                "Name": "自定义线路",
                "Key": "customline",
                "LimitCount": 9999,
                "UseCount": 1
            },
            {
                "Name": "D 监控备用 IP",
                "Key": "dmonitor_ip",
                "LimitCount": 25,
                "UseCount": 0
            }
        ]
    }
}
```

