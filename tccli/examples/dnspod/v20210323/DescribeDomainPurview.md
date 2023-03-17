**Example 1: 获取域名权限**

 获取域名权限

Input: 

```
tccli dnspod DescribeDomainPurview --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "PurviewList": [
            {
                "Name": "URL转发条数",
                "Value": "10"
            },
            {
                "Name": "NS记录条数",
                "Value": "1999"
            },
            {
                "Name": "AAAA记录条数",
                "Value": "1999"
            },
            {
                "Name": "SRV记录条数",
                "Value": "1999"
            },
            {
                "Name": "域名别名绑定个数",
                "Value": "10"
            },
            {
                "Name": "域名锁定天数",
                "Value": "365"
            },
            {
                "Name": "域名共享个数",
                "Value": "1000"
            },
            {
                "Name": "子域名级数",
                "Value": "12"
            },
            {
                "Name": "泛解析级数",
                "Value": "10"
            },
            {
                "Name": "负载均衡数量",
                "Value": "60"
            },
            {
                "Name": "记录TTL最低",
                "Value": "1"
            },
            {
                "Name": "混合泛解析支持",
                "Value": "yes"
            },
            {
                "Name": "增强线路类型",
                "Value": "yes"
            },
            {
                "Name": "分省线路类型",
                "Value": "yes"
            },
            {
                "Name": "分大洲线路类型",
                "Value": "yes"
            }
        ]
    }
}
```

