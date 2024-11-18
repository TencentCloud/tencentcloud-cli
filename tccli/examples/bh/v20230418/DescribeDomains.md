**Example 1: 查询网络域**

查询网络域

Input: 

```
tccli bh DescribeDomains --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DomainSet": [
            {
                "Id": 7,
                "DomainId": "net-vvr396q5",
                "DomainName": "test-net-name",
                "Enabled": 1,
                "Status": 0,
                "ResourceId": "bh-saas-jtvukub4",
                "CreateTime": "2024-04-19T11:11:55+08:00",
                "Default": 0,
                "WhiteIpSet": [
                    "127.0.0.1",
                    "171.0.0.1"
                ]
            }
        ],
        "RequestId": "sdfsadf-sdfasd-sdfsad-sdf2222",
        "TotalCount": 1
    }
}
```

