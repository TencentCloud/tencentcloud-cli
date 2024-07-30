**Example 1: 获取资源组信息**



Input: 

```
tccli cdwdoris DescribeWorkloadGroup --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "WorkloadGroups": [
            {
                "WorkloadGroupName": "abc",
                "CpuShare": 10,
                "MemoryLimit": 10,
                "EnableMemoryOverCommit": true
            }
        ],
        "Status": "abc",
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

