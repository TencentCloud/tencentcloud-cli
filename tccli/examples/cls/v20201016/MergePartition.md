**Example 1: 合并主题分区**



Input: 

```
tccli cls MergePartition --cli-unfold-argument  \
    --TopicId 427bba81-e149-4a8b-bd0d-b2a412520d7b \
    --PartitionId 2
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "PartitionId": 2,
                "Status": "readonly",
                "InclusiveBeginKey": "0000",
                "ExclusiveEndKey": "7fff",
                "CreateTime": "2019-01-14 19:25:41",
                "LastWriteTime": "2019-01-14 19:33:41"
            },
            {
                "PartitionId": 3,
                "Status": "readonly",
                "InclusiveBeginKey": "7fff",
                "ExclusiveEndKey": "ffff",
                "CreateTime": "2019-01-14 19:25:41",
                "LastWriteTime": "2019-01-14 19:33:41"
            },
            {
                "PartitionId": 4,
                "Status": "readwrite",
                "InclusiveBeginKey": "0000",
                "ExclusiveEndKey": "ffff",
                "CreateTime": "2019-01-14 19:33:41",
                "LastWriteTime": null
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

