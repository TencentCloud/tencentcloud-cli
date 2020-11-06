**Example 1: 创建四层监听器**



Input: 

```
tccli bmlb CreateL4Listeners --cli-unfold-argument  \
    --LoadBalancerId lb-m1i50ynj \
    --ListenerSet.0.LoadBalancerPort 1000 \
    --ListenerSet.0.Protocol tcp \
    --ListenerSet.0.ListenerName 1000 \
    --ListenerSet.0.SessionExpire 0
```

Output: 
```
{
    "Response": {
        "TaskId": "2385671",
        "RequestId": "dbcca4e7-6491-49bc-8814-d7c2635d242c"
    }
}
```

