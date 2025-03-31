**Example 1: 设置维护时间窗**

修改指定实例的维护时间窗

Input: 

```
tccli vdb ModifyInstanceMaintenanceWindow --cli-unfold-argument  \
    --InstanceId vdb-jnaj**** \
    --StartTime 01:00 \
    --TimeSpan 2
```

Output: 
```
{
    "Response": {
        "RequestId": "21e24cbd-0013-42c3-a2f5-81e5cae0b442"
    }
}
```

