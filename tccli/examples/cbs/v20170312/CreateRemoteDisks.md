**Example 1: 创建弹性单副本SSD硬盘**

创建并挂载一块弹性单副本SSD硬盘到指定实例。

Input: 

```
tccli cbs CreateRemoteDisks --cli-unfold-argument  \
    --InstanceId ins-23kmz0bd \
    --DiskSize 2000 \
    --DiskChargeType PREPAID \
    --Placement.Zone ap-qingyuan-1 \
    --DiskCount 1 \
    --DiskName helloworld \
    --DiskChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a285b92a-3328-42d0-90df-3aa663c6cb76"
    }
}
```

