**Example 1: 修改数据订阅通道的订阅规则**

修改数据订阅的订阅规则，如添加或者移除某些库表

Input: 

```
tccli dts ModifySubscribeObjects --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e \
    --SubscribeObjectType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb",
        "AsyncRequestId": "19b514a7-816c43c1-ffb34ab6-8c6a23eb"
    }
}
```

