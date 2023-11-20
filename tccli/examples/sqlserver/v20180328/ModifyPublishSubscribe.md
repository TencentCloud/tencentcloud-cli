**Example 1: 修改实例的发布订阅关系**



Input: 

```
tccli sqlserver ModifyPublishSubscribe --cli-unfold-argument  \
    --InstanceId mssql-2cwisu23 \
    --PublishSubscribeId 5 \
    --DatabaseTupleSet.0.DatabaseTuple.PublishDatabase db1 \
    --DatabaseTupleSet.0.DatabaseTuple.SubscribeDatabase db1 \
    --DatabaseTupleSet.0.NewDatabaseTuple.PublishDatabase db2 \
    --DatabaseTupleSet.0.NewDatabaseTuple.SubscribeDatabase db2
```

Output: 
```
{
    "Response": {
        "FlowId": 110,
        "RequestId": "133c6f22-f562-4107-8458-c3b25c901918"
    }
}
```

**Example 2: 删除实例的发布订阅关系**



Input: 

```
tccli sqlserver ModifyPublishSubscribe --cli-unfold-argument  \
    --InstanceId mssql-2cwisu23 \
    --PublishSubscribeId 5 \
    --DatabaseTupleSet.0.DatabaseTuple.PublishDatabase db1 \
    --DatabaseTupleSet.0.DatabaseTuple.SubscribeDatabase db1 \
    --DatabaseTupleSet.0.DeleteDataBasesTuple true
```

Output: 
```
{
    "Response": {
        "FlowId": 111,
        "RequestId": "133c6f22-f562-4107-8458-c3b25c901918"
    }
}
```

