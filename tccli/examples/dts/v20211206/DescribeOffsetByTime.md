**Example 1: 根据时间查询kafka中的checkpoint消息**

查询KafkaTopic中指定时间前最近的checkpoint及其offset

Input: 

```
tccli dts DescribeOffsetByTime --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --Time 2023-05-15 16:31:30
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Offset": 62856,
                "PartitionNo": 0
            },
            {
                "Offset": 62842,
                "PartitionNo": 1
            },
            {
                "Offset": 62842,
                "PartitionNo": 2
            },
            {
                "Offset": 62842,
                "PartitionNo": 3
            }
        ],
        "RequestId": "087e2780-f3bc-11ed-8dff-ff5f3734b02b"
    }
}
```

