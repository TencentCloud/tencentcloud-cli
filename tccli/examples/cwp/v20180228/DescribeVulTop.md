**Example 1: 漏洞top统计**

漏洞top统计

Input: 

```
tccli cwp DescribeVulTop --cli-unfold-argument  \
    --Top 5
```

Output: 
```
{
    "Response": {
        "RequestId": "f14ce73f-50d7-4c36-af1d-fc33dae510c4",
        "VulTopList": [
            {
                "VulName": "Linux口令过期后账号最长有效天数策略",
                "VulLevel": 1,
                "VulCount": 27,
                "VulId": 1028
            },
            {
                "VulName": "Linux未配置账户登录失败锁定策略",
                "VulLevel": 2,
                "VulCount": 17,
                "VulId": 1028
            }
        ]
    }
}
```

