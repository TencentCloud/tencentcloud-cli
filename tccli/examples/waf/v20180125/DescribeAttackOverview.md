**Example 1: 获取指定时间段内请求总数**

获取指定时间段内请求总数，这个接口不需要客户购买日志服务

Input: 

```
tccli waf DescribeAttackOverview --cli-unfold-argument  \
    --FromTime 2023-02-06 00:00:00 \
    --ToTime 2023-02-06 23:59:59
```

Output: 
```
{
    "Response": {
        "AccessCount": 158,
        "AttackCount": 98,
        "ACLCount": 0,
        "CCCount": 0,
        "BotCount": 0,
        "ApiAssetsCount": 1,
        "RequestId": "8a3b7134-77f9-4ee5-b30e-73809ccad10f"
    }
}
```

