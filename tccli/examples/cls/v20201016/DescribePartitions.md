**Example 1: 获取分区列表**



Input: 

```
tccli cls DescribePartitions --cli-unfold-argument  \
    --TopicId cabcd0a8-4a54-11eb-b378-0242ac130002
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "PartitionId": 1,
                "Status": "readwrite",
                "InclusiveBeginKey": "0000",
                "ExclusiveEndKey": "ffff",
                "CreateTime": "2019-01-14 19:19:41",
                "LastWriteTime": null
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

