**Example 1: 获取Kakfa协议消费信息**



Input: 

```
tccli cls DescribeKafkaConsumer --cli-unfold-argument  \
    --FromTopicId a5ce0c9c-0690-44a5-bc79-5f2190626bd0
```

Output: 
```
{
    "Response": {
        "Status": true,
        "TopicID": "out-a5ce0c9c-0690-44a5-bc79-5f2190626bd0",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "Compression": 1
    }
}
```

