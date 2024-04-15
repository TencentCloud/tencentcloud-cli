**Example 1: 发布列表**



Input: 

```
tccli lke ListRelease --cli-unfold-argument  \
    --BotBizId 1714970520775950336 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Desc": "测试下发布哈哈哈哈哈哈哈哈",
                "FailCount": 0,
                "Operator": "stanwei",
                "Reason": "",
                "ReleaseBizId": "1730138654150348800",
                "Status": 3,
                "StatusDesc": "发布成功",
                "SuccessCount": 6,
                "UpdateTime": "1701332268"
            }
        ],
        "RequestId": "e28f31fe-72a3-459b-9abb-5042a0f35a1b",
        "Total": "1"
    }
}
```

