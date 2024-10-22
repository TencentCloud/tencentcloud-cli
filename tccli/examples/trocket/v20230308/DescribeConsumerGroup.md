**Example 1: 查询消费组详情**

查询消费者详情

Input: 

```
tccli trocket DescribeConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup group
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ConsumeEnable": true,
        "ConsumeMessageOrderly": false,
        "ConsumeType": "PUSH",
        "ConsumerLag": 1580,
        "ConsumerNum": 2,
        "CreatedTime": 1683613488000,
        "MaxRetryTimes": 16,
        "Remark": "测试消费组",
        "RequestId": "bc4ffab1-65cc-4ef6-9114-0de06c333b84",
        "Tps": 60
    }
}
```

