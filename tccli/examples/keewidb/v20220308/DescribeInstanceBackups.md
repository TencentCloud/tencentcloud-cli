**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceBackups --cli-unfold-argument  \
    --InstanceId kee-i0krexg9 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BackupRecord": [
            {
                "BackupId": "",
                "BackupType": "1",
                "Locked": 0,
                "Remark": "",
                "StartTime": "2022-08-28 16:00:07",
                "Status": 2
            },
            {
                "BackupId": "",
                "BackupType": "1",
                "Locked": 0,
                "Remark": "",
                "StartTime": "2022-08-27 16:00:57",
                "Status": 2
            },
            {
                "BackupId": "",
                "BackupType": "1",
                "Locked": 0,
                "Remark": "",
                "StartTime": "2022-08-26 16:00:43",
                "Status": 2
            }
        ],
        "BackupSet": [],
        "RequestId": "1bb3c529-3db5-4bca-9f2b-4c04f919adf5",
        "TotalCount": 3
    }
}
```

