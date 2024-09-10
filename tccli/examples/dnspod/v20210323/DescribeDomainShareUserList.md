**Example 1: 获取指定域名的已共享列表**

获取指定域名的已共享列表

Input: 

```
tccli dnspod DescribeDomainShareUserList --cli-unfold-argument  \
    --Domain example.com
```

Output: 
```
{
    "Response": {
        "RequestId": "1dbb40a1-8834-43e2-bae0-c5e2d0823944",
        "DomainShareList": [
            {
                "DomainShareId": 21253,
                "Mode": "rw",
                "Nickname": "我的测试环境企业",
                "QCloudUIN": "700000283316",
                "Status": "enabled",
                "SubDomain": ""
            }
        ]
    }
}
```

