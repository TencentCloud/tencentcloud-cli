**Example 1: 修改资源组信息**



Input: 

```
tccli cdwdoris ModifyWorkloadGroup --cli-unfold-argument  \
    --InstanceId abc \
    --WorkloadGroup.WorkloadGroupName abc \
    --WorkloadGroup.CpuShare 10 \
    --WorkloadGroup.MemoryLimit 10 \
    --WorkloadGroup.EnableMemoryOverCommit True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

