**Example 1: 创建资源组**



Input: 

```
tccli cdwdoris CreateWorkloadGroup --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx \
    --WorkloadGroup.WorkloadGroupName group_name \
    --WorkloadGroup.CpuShare 10 \
    --WorkloadGroup.MemoryLimit 20 \
    --WorkloadGroup.EnableMemoryOverCommit True
```

Output: 
```
{
    "Response": {
        "RequestId": "abxadsfc"
    }
}
```

