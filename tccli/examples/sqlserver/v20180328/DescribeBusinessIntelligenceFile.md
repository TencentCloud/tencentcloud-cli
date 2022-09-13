**Example 1: 查询商业智能服务需要的文件**



Input: 

```
tccli sqlserver DescribeBusinessIntelligenceFile --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderByType desc \
    --OrderBy create_time \
    --InstanceId mssqlbi-fo2dwujt \
    --FileName test \
    --FileType FLAT \
    --StatusSet 1
```

Output: 
```
{
    "Response": {
        "BackupMigrationSet": [
            {
                "Action": {
                    "AllAction": [
                        "view",
                        "remark",
                        "delete"
                    ],
                    "AllowedAction": [
                        "view",
                        "remark",
                        "delete"
                    ]
                },
                "CreateTime": "2022-08-05 14:14:17",
                "EndTime": "0000-00-00 00:00:00",
                "FileMd5": "",
                "FileName": "test.xlsx",
                "FilePath": "D:\\SSIS\\",
                "FileSize": 0,
                "FileType": "FLAT",
                "FileURL": "http://sqlserver-gz-test-1251966477.cos.ap-guangzhou.myqcloud.com/test.xlsx",
                "InstanceId": "mssqlbi-fo2dwujt",
                "Message": "",
                "Remark": "Remark",
                "StartTime": "0000-00-00 00:00:00",
                "Status": 1
            }
        ],
        "RequestId": "13903852-75f7-4977-9965-aa4babeadbd5",
        "TotalCount": 1
    }
}
```

