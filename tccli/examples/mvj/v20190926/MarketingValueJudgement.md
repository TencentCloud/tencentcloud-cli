**Example 1: 营销价值判断正确返回示例**



Input: 

```
tccli mvj MarketingValueJudgement --cli-unfold-argument  \
    --AccountType 4 \
    --Uid 17620430702 \
    --UserIp 117.62.203.111 \
    --PostTime 1569486063 \
    --Imei 861622010000056 \
    --Referer 1569571332
```

Output: 
```
{
    "Response": {
        "Data": {
            "PostTime": 1569486063,
            "Uid": "17620430702",
            "UserIp": "117.62.203.111",
            "ValueScore": 84
        },
        "RequestId": "ab49be72-fac8-467d-bf59-9c6193fe5af6"
    }
}
```

**Example 2: 营销价值判断错误返回示例**



Input: 

```
tccli mvj MarketingValueJudgement --cli-unfold-argument  \
    --AccountType 4 \
    --Uid 1620430702 \
    --UserIp 117.62.203.111 \
    --PostTime 1569486063 \
    --Imei 861622010000056 \
    --Referer 1569571332
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.AccountNotFound",
            "Message": "未开通账号！"
        },
        "RequestId": "8ce8d3dd-d849-4bc4-9fa0-2868749164eb"
    }
}
```

