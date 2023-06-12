**Example 1: 配置数据订阅自动续费标识**

配置数据订阅自动续费标识

Input: 

```
tccli dts ModifySubscribeAutoRenewFlag --cli-unfold-argument  \
    --SubscribeId subs-8392jd821u \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

