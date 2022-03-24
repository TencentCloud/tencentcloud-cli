**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceBackups --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0 \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "RequestId": "2d4387ee-2011-449e-a32b-87f9366f3ef4",
        "TotalCount": 2,
        "BackupSet": [
            {
                "StartTime": "2018-09-04 12:51:21",
                "BackupId": "2e4127f8-affe-11e8-941e-4846fb00c75d",
                "BackupType": "0",
                "Status": 2,
                "Remark": "测试使用",
                "Locked": 0,
                "BackupSize": 543534435,
                "FullBackup": 0,
                "InstanceType": 6
            },
            {
                "StartTime": "2018-09-04 12:53:06",
                "BackupId": "6cbbf53a-affe-11e8-905b-4846fb00c75d",
                "BackupType": "0",
                "Status": 2,
                "Remark": "xxx",
                "Locked": 0,
                "BackupSize": 3124324,
                "FullBackup": 0,
                "InstanceType": 7
            }
        ]
    }
}
```

