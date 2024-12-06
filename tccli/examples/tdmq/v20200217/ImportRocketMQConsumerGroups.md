**Example 1: 导入消费组列表**

导入消费组列表

Input: 

```
tccli tdmq ImportRocketMQConsumerGroups --cli-unfold-argument  \
    --Groups.0.Namespace test_ns \
    --Groups.0.GroupName test_group \
    --Groups.0.ConsumeBroadcastEnable True \
    --Groups.0.ConsumeEnable True \
    --Groups.0.Remark remark info \
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

