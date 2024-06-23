**Example 1: 查询数据库实例升级类型**



Input: 

```
tccli cdb DescribeInstanceUpgradeType --cli-unfold-argument  \
    --InstanceId cdb-xxxxx \
    --DstCpu 1 \
    --DstMemory 1000 \
    --DstDisk 200 \
    --DstVersion 8.0 \
    --DstProtectMode 0 \
    --DstDeployMode 0 \
    --DstSlaveZone 100003 \
    --DstBackupZone 0 \
    --DstCdbType CUSTOM
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "InstanceId": "cdb-xxx",
        "UpgradeType": "Trsf"
    }
}
```

