**Example 1: 下线已隔离的数据订阅实例**

订阅任务已经隔离，立即发起下线任务

Input: 

```
tccli dts DestroyIsolatedSubscribe --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw
```

Output: 
```
{
    "Response": {
        "RequestId": "14a719b5-ffb34ab6-816c43c1-8c6a23eb"
    }
}
```

