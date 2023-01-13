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
        "RequestId": "66de08ce-ea4e-43c0-be85-90b7549293c5",
        "RunningSavepoint": [],
        "RunningTotalNumber": 0,
        "Savepoint": [
            {
                "Id": 0,
                "SerialId": "cql-asdf5678",
                "VersionId": 1,
                "JobRuntimeId": 6029,
                "Status": 1,
                "CreateTime": 1638198485,
                "UpdateTime": 1638198486,
                "Path": "cosn://helloworld-guangzhou-12345/1234567890/100000000006/cql-asdf5678/2/flink-savepoints/savepoint-000000-9085e69e28c4",
                "Size": 816,
                "RecordType": 3,
                "TimeConsuming": 1,
                "Timeout": 1200,
                "Description": "作业停止时自动生成的快照"
            }
        ],
        "TotalNumber": 1
    }
}
```

