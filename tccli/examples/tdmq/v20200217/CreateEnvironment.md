**Example 1: 创建命名空间**

是否开启自动创建订阅

Input: 

```
tccli tdmq CreateEnvironment --cli-unfold-argument  \
    --EnvironmentId test1 \
    --MsgTTL 100 \
    --AutoSubscriptionCreation True \
    --ClusterId pulsar-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "test1",
        "NamespaceId": "namespace-8893gp3428",
        "MsgTTL": 100,
        "Remark": "",
        "RequestId": "0843ea4f-d6ba-463b-952c-75708a7e8901"
    }
}
```

