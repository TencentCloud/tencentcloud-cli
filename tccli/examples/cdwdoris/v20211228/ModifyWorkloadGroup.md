**Example 1: 修改资源组信息**



Input: 

```
tccli cdwdoris ModifyWorkloadGroup --cli-unfold-argument  \
    --InstanceId cdwdoris-qliqegj3 \
    --WorkloadGroup.WorkloadGroupName group1 \
    --WorkloadGroup.CpuShare 10 \
    --WorkloadGroup.MemoryLimit 10 \
    --WorkloadGroup.EnableMemoryOverCommit True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "117ad1ab-8571-4085-8356-382b6a5f07f6"
    }
}
```

