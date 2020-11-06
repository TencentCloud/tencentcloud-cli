**Example 1: 创建发布订阅**



Input: 

```
tccli sqlserver CreatePublishSubscribe --cli-unfold-argument  \
    --PublishSubscribeName Create_name \
    --PublishInstanceId mssql-2cwisu23 \
    --SubscribeInstanceId mssql-hlh6yka1 \
    --DatabaseTupleSet.0.PublishDatabase db1 \
    --DatabaseTupleSet.0.SubscribeDatabase db1
```

Output: 
```
{
    "Response": {
        "FlowId": 1002591,
        "RequestId": "6353b539-bcd4-41fa-8d6a-98c94601f77d"
    }
}
```

