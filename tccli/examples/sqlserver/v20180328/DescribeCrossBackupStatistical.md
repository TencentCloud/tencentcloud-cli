**Example 1: 查询跨地域备份实时统计列表**



Input: 

```
tccli sqlserver DescribeCrossBackupStatistical --cli-unfold-argument  \
    --InstanceIdSet mssql-6upluvd5 \
    --InstanceNameSet name \
    --CrossBackupStatus enable \
    --CrossRegion guangzhou \
    --OrderBy default \
    --OrderByType desc \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1fed8472-f117-11ec-be47-525400853186",
        "TotalCount": 1,
        "Items": [
            {
                "ActualUsedCount": 4937,
                "ActualUsedSpace": 554778704,
                "CrossBackupEnabled": "enable",
                "CrossBackupSaveDays": 7,
                "CrossRegions": [
                    "ap-shanghai"
                ],
                "DataBackupCount": 1019,
                "DataBackupSpace": 550868544,
                "InstanceId": "mssql-1ybz12wb",
                "LastBackupStartTime": "2022-06-21 13:57:17",
                "LogBackupCount": 3918,
                "LogBackupSpace": 3910160,
                "Name": "xinyuanxu-new",
                "Region": "ap-guangzhou",
                "Status": 2
            }
        ]
    }
}
```

