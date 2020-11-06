**Example 1: 下线已隔离的数据订阅实例**

订阅实例已经在隔离中，立即发起下线任务

Input: 

```
tccli dts OfflineIsolatedSubscribe --cli-unfold-argument  \
    --SubscribeId subs-ieuwi83j2e
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

