**Example 1: 示例**

查询指定批量升级固件任务的详情

Input: 

```
tccli iotexplorer DescribeFirmwareTask --cli-unfold-argument  \
    --ProductID product \
    --FirmwareVersion 1.0.0 \
    --TaskId 1000
```

Output: 
```
{
    "Response": {
        "TaskId": 1000,
        "ProductId": "product",
        "ProductName": "name",
        "CreatorNickName": "leo",
        "Status": 5,
        "Type": 1,
        "CreateTime": 1791206390,
        "CreateUserId": 2362445,
        "UpgradeMode": "filename",
        "OriginalVersion": "1.0.0",
        "UpgradeMethod": 0,
        "DelayTime": 0,
        "TimeoutInterval": 86400,
        "MaxRetryNum": 3,
        "RetryInterval": 60,
        "OverrideMode": 0,
        "FwType": "mcu",
        "TaskUserDefine": "{\"key\":\"value\"}",
        "RateLimit": 1000,
        "StartTime": 1791206400,
        "EndTime": 1791811200,
        "RequestId": "3c11474f-9501-482f-8b59-97213b8779d4"
    }
}
```

