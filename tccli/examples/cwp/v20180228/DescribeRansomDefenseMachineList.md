**Example 1: 查询备份详情列表**

查询备份详情列表

Input: 

```
tccli cwp DescribeRansomDefenseMachineList --cli-unfold-argument  \
    --Order DESC \
    --Limit 1 \
    --By LastBackupTime \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "MachineName": "销售许可测试机器",
                "InstanceId": "ins-ewwewe",
                "MachineIp": "10.0.0.2",
                "MachineWanIp": "xx.xx.xx.xx",
                "CloudTags": [],
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionCode": "gz",
                    "RegionId": 1,
                    "RegionName": "华南地区（广州）",
                    "RegionNameEn": "South China (Guangzhou)"
                },
                "Tag": [
                    {
                        "Rid": 16069,
                        "Name": "apitest",
                        "TagId": 16069
                    }
                ],
                "Status": 1,
                "StrategyId": 5570,
                "StrategyName": "tt1",
                "DiskInfo": "diskId1|diskName1;diskId2|diskName2",
                "HostVersion": 2,
                "BackupCount": 128,
                "BackupSuccessCount": 121,
                "LastBackupStatus": 1,
                "LastBackupTime": "2024-10-22 00:04:04",
                "LastBackupMessage": "success",
                "RollBackStatus": 0,
                "RollBackPercent": 0
            }
        ],
        "RequestId": "586e7838-8dce-38d4-5e4d-bbc5f4191c25"
    }
}
```

