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
                "VulCount": 27
            },
            {
                "VulName": "Linux未配置账户登录失败锁定策略",
                "VulLevel": 2,
                "VulCount": 17
            },
            {
                "VulName": "Linux帐户超时自动登出配置",
                "VulLevel": 2,
                "VulCount": 17
            },
            {
                "VulName": "Linux帐户口令生存期策略",
                "VulLevel": 2,
                "VulCount": 17
            },
            {
                "VulName": "限制root权限用户远程登录",
                "VulLevel": 2,
                "VulCount": 17
            }
        ]
    }
}
```

