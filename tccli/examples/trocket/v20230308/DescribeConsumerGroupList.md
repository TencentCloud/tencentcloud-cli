**Example 1: 获取消费组列表**

获取消费组列表

Input: 

```
tccli trocket DescribeConsumerGroupList --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ConsumeEnable": true,
                "ConsumeMessageOrderly": true,
                "ConsumerGroup": "group",
                "InstanceId": "rmq-72mo3a9o",
                "MaxRetryTimes": 16,
                "Remark": "test"
            }
        ],
        "RequestId": "318142bf-0dd1-4b81-9444-a40f988619a1",
        "TotalCount": 7
    }
}
```

