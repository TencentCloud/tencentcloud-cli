**Example 1: DescribeCOSTaskResult**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTaskResult --cli-unfold-argument  \
    --DspaId xx \
    --Limit 0 \
    --Filters.0.Name BucketName \
    --Filters.0.Values bucket_1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "TotalCount": 1,
        "Items": [
            {
                "BucketResultId": 3,
                "TaskId": 28,
                "TaskName": "898111",
                "BucketName": "bucket_1",
                "TotalFiles": 2,
                "SensitiveDataNums": 6
            }
        ]
    }
}
```

