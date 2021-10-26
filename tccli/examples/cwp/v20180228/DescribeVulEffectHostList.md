**Example 1: 漏洞影响主机列表**

漏洞影响主机列表

Input: 

```
tccli cwp DescribeVulEffectHostList --cli-unfold-argument  \
    --VulId 100435 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "TotalCount": 2,
        "VulEffectHostList": [
            {
                "EventId": 15,
                "Status": 0,
                "LastTime": "2020-04-22 03:29:52",
                "Level": 1,
                "Quuid": "b86925b4-cc36-420e-80d4-5094cb2f094b",
                "Uuid": "ed629672-165e-11ea-8bcf-40f2e9f3d932",
                "HostIp": "10.104.14.165",
                "AliasName": "poc测试(129.204.36.227)",
                "Tags": null
            },
            {
                "EventId": 16,
                "Status": 1,
                "LastTime": "2020-02-09 03:02:17",
                "Level": 2,
                "Quuid": "b86925b4-cc36-420e-80d4-5094cb2f094b",
                "Uuid": "ed629672-165e-11ea-8bcf-40f2e9f3d932",
                "HostIp": "10.104.14.165",
                "AliasName": "poc测试(129.204.36.227)",
                "Tags": null
            }
        ]
    }
}
```

