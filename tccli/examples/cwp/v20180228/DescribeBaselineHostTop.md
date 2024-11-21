**Example 1: 服务器风险top接口**

查询服务器风险top接口

Input: 

```
tccli cwp DescribeBaselineHostTop --cli-unfold-argument  \
    --Top 5 \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "BaselineHostTopList": [
            {
                "HostName": "1号主机",
                "Quuid": "a0770b41-9697-4a1d-8150-b8fa247b6*****",
                "Score": 1002,
                "EventLevelList": [
                    {
                        "EventLevel": 2,
                        "EventCount": 28
                    }
                ]
            }
        ]
    }
}
```

