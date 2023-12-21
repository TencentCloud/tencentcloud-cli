**Example 1: 修改按量实例系统盘介质**

修改实例系统盘介质，从本地盘转化成普通云硬盘。

Input: 

```
tccli cvm ModifyInstanceDiskType --cli-unfold-argument  \
    --InstanceId ins-r8hr2upy \
    --SystemDisk.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

