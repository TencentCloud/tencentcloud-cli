**Example 1: 修改数据订阅自动续费标识**

将一个包年包月的订阅任务从不自动续费改为自动续费

Input: 

```
tccli dts ModifySubscribeAutoRenewFlag --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
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

