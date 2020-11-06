**Example 1: 删除发布订阅**



Input: 

```
tccli sqlserver DeletePublishSubscribe --cli-unfold-argument  \
    --PublishSubscribeId 5 \
    --DatabaseTupleSet.0.PublishDatabase test01 \
    --DatabaseTupleSet.0.SubscribeDatabase test02
```

Output: 
```
{
    "Response": {
        "RequestId": "2941128b-d8fb-4af4-bb73-d79c413e1a7d"
    }
}
```

