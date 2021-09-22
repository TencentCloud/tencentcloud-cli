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
        "RequestId": "req-566234234",
        "BaselineHostTopList": [
            {
                "HostName": "1号主机"
            }
        ]
    }
}
```

