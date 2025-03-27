**Example 1: 查询固件升级任务详情**



Input: 

```
tccli iotvideo DescribeFirmwareTask --cli-unfold-argument  \
    --ProductID product \
    --FirmwareVersion 1.0.0 \
    --TaskId 10000
```

Output: 
```
{
    "Response": {
        "TaskId": 1000175,
        "Status": 3,
        "CreateTime": 1589466879,
        "Type": 1,
        "ProductName": "门锁",
        "OriginalVersion": "1.1.1",
        "UpgradeMode": "originalVersion",
        "ProductId": "product",
        "RequestId": "id"
    }
}
```

