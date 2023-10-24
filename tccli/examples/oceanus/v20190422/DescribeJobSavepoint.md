**Example 1: 1**



Input: 

```
tccli oceanus DescribeJobSavepoint --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --JobId cql-asdf5678
```

Output: 
```
{
    "Response": {
        "TotalNumber": 0,
        "Savepoint": [
            {
                "Id": 0,
                "VersionId": 0,
                "Status": 0,
                "CreateTime": 0,
                "UpdateTime": 0,
                "Path": "abc",
                "Size": 0,
                "RecordType": 0,
                "JobRuntimeId": 0,
                "Description": "abc",
                "Timeout": 0,
                "SerialId": "abc",
                "TimeConsuming": 0,
                "PathStatus": 0
            }
        ],
        "RunningSavepoint": [
            {
                "Id": 0,
                "VersionId": 0,
                "Status": 0,
                "CreateTime": 0,
                "UpdateTime": 0,
                "Path": "abc",
                "Size": 0,
                "RecordType": 0,
                "JobRuntimeId": 0,
                "Description": "abc",
                "Timeout": 0,
                "SerialId": "abc",
                "TimeConsuming": 0,
                "PathStatus": 0
            }
        ],
        "RunningTotalNumber": 0,
        "RequestId": "abc"
    }
}
```

