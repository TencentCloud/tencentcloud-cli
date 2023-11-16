**Example 1: 查询备份实时统计列表**



Input: 

```
tccli sqlserver DescribeBackupStatistical --cli-unfold-argument  \
    --InstanceIdSet mssql-3l3fgqn7 \
    --InstanceNameSet 数仓 \
    --Offset 0 \
    --Limit 3 \
    --OrderBy data \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ActualUsedSpace": 1003844420,
                "AutoBackupCount": 9190,
                "AutoBackupSpace": 920300548,
                "DataBackupCount": 1706,
                "DataBackupSpace": 996004980,
                "InstanceId": "mssql-1ybz12wb",
                "LogBackupCount": 7627,
                "LogBackupSpace": 7839440,
                "ManualBackupCount": 143,
                "ManualBackupSpace": 83543872,
                "Name": "xinyuanxu-new",
                "Region": "ap-guangzhou",
                "RegionId": 1,
                "Status": 2
            }
        ],
        "RequestId": "c3ea3ea0-f0a2-11ec-94dd-525400853186",
        "TotalCount": 17
    }
}
```

