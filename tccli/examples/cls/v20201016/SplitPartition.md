**Example 1: 主题分区分裂**



Input: 

```
tccli cls SplitPartition --cli-unfold-argument  \
    --TopicId 427bba81-e149-4a8b-bd0d-b2a412520d7b \
    --PartitionId 1 \
    --Number 2
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "PartitionId": 1,
                "Status": "readonly",
                "InclusiveBeginKey": "0000",
                "ExclusiveEndKey": "ffff",
                "CreateTime": "2019-01-14 19:25:41",
                "LastWriteTime": "2019-01-14 19:33:41"
            },
            {
                "PartitionId": 2,
                "Status": "readwrite",
                "InclusiveBeginKey": "0000",
                "ExclusiveEndKey": "7fff",
                "CreateTime": "2019-01-14 19:25:41",
                "LastWriteTime": "2019-01-14 19:33:41"
            },
            {
                "PartitionId": 3,
                "Status": "readwrite",
                "InclusiveBeginKey": "7fff",
                "ExclusiveEndKey": "ffff",
                "CreateTime": "2019-01-14 19:33:41",
                "LastWriteTime": null
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

