**Example 1: 查询Trino(PrestoSQL)查询信息**



Input: 

```
tccli emr DescribeTrinoQueryInfo --cli-unfold-argument  \
    --InstanceId emr-d82w3t9p \
    --PageSize 10 \
    --StartTime 1701792000 \
    --EndTime 1701878399 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "QueryInfoList": [
            {
                "Catalog": "hive",
                "ClientIpAddr": "10.0.1.104",
                "CompletedSplits": "",
                "CpuTime": 0,
                "CumulativeMemory": 0,
                "DurationMillis": 0,
                "EndTime": 0,
                "Id": "20240708_111543_00007_lcmdbi8z",
                "InternalNetworkBytes": 0,
                "OutputBytes": 0,
                "PeakUserMemoryBytes": 0,
                "PhysicalInputBytes": 0,
                "ProcessedInputBytes": 0,
                "SqlCompileTime": 0,
                "StartTime": 0,
                "State": "QUEUED",
                "Statement": "create table impala_ranger",
                "User": "hadoop",
                "WrittenBytes": 0
            }
        ],
        "RequestId": "cfbbbe0f-5d30-4bf7-b87b-428b14ac3ws22",
        "TotalCount": 18
    }
}
```

