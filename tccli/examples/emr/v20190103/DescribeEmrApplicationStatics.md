**Example 1: 【监控】查询Appilication统计V2**



Input: 

```
tccli emr DescribeEmrApplicationStatics --cli-unfold-argument  \
    --InstanceId emr-9kd5tnmq
```

Output: 
```
{
    "Response": {
        "ApplicationTypes": [
            "MAPREDUCE"
        ],
        "Queues": [
            "root.default"
        ],
        "RequestId": "12345678",
        "Statics": [
            {
                "Queue": "root.default",
                "User": "hadoop",
                "ApplicationType": "MAPREDUCE",
                "SumMemorySeconds": 58250,
                "SumVCoreSeconds": 33,
                "SumHDFSBytesWritten": "48 bytes",
                "SumHDFSBytesRead": "269 bytes",
                "CountApps": 0
            }
        ],
        "TotalCount": 1,
        "Users": [
            "hadoop"
        ]
    }
}
```

