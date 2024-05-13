**Example 1: DescribeCOSTaskResult**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTaskResult --cli-unfold-argument  \
    --DspaId abc \
    --Offset 0 \
    --Limit 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BucketResultId": 0,
                "TaskId": 0,
                "TaskName": "abc",
                "ResultId": 0,
                "DataSourceId": "abc",
                "BucketName": "abc",
                "TotalFiles": 0,
                "SensitiveDataNums": 0,
                "EndTime": "abc",
                "DataSourceName": "abc",
                "Status": 0,
                "ErrorInfo": "abc",
                "ResourceRegion": "abc",
                "OverSize": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

