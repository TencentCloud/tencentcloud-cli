**Example 1: 标准调用**

标准调用

Input: 

```
tccli tdmq ImportRocketMQConsumerGroups --cli-unfold-argument  \
    --Groups.0.Namespace tdmq_default \
    --Groups.0.GroupName ConsumerGroup_29106 \
    --Groups.0.ConsumeBroadcastEnable True \
    --Groups.0.ConsumeEnable True \
    --TaskId 700000780521-migratetest-d93e34d2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "f324d108-56ba-4527-822a-4f73283388b1"
    }
}
```

**Example 2: 导入消费组列表**

导入消费组列表

Input: 

```
tccli tdmq ImportRocketMQConsumerGroups --cli-unfold-argument  \
    --Groups.0.Namespace  \
    --Groups.0.GroupName ConsumerGroup_1039 \
    --Groups.0.ConsumeBroadcastEnable True \
    --Groups.0.ConsumeEnable True \
    --Groups.0.Remark abc \
    --Groups.0.ConsumerGroupType TCP \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "78ef8089-2ec3-4784-ad21-68c71d289d69"
    }
}
```

