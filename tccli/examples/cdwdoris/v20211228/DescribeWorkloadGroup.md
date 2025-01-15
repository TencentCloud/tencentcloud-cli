**Example 1: 获取资源组信息**



Input: 

```
tccli cdwdoris DescribeWorkloadGroup --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "758726a5-3bdb-40ac-a77a-938ca3bde664",
        "Status": "close",
        "WorkloadGroups": [
            {
                "CpuHardLimit": "-1",
                "CpuShare": 100,
                "EnableMemoryOverCommit": true,
                "MemoryLimit": -1,
                "WorkloadGroupName": "_internal"
            },
            {
                "CpuHardLimit": "-1",
                "CpuShare": 1024,
                "EnableMemoryOverCommit": true,
                "MemoryLimit": 30,
                "WorkloadGroupName": "normal"
            }
        ]
    }
}
```

