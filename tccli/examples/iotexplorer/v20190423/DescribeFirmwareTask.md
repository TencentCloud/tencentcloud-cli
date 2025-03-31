**Example 1: 查询固件升级任务详情**

查询固件升级任务详情

Input: 

```
tccli iotexplorer DescribeFirmwareTask --cli-unfold-argument  \
    --TaskId 1 \
    --FirmwareVersion 1.0.0 \
    --ProductID J2CRPPZ8J4
```

Output: 
```
{
    "Response": {
        "RequestId": "3c11474f-9501-482f-8b59-97213b8779d4",
        "UpgradeMode": "filename",
        "ProductName": "name",
        "CreateUserId": 2362445,
        "ProductId": "J2CRPPZ8J4",
        "Type": 1,
        "TaskId": 1,
        "CreateTime": 1686291740,
        "OriginalVersion": "v1",
        "CreatorNickName": "leo",
        "Status": 5
    }
}
```

