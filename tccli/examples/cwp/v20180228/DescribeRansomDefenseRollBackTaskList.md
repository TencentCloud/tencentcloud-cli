**Example 1: 查询回滚任务列表**

查询回滚任务列表

Input: 

```
tccli cwp DescribeRansomDefenseRollBackTaskList --cli-unfold-argument  \
    --Order DESC \
    --Limit 1 \
    --By ModifyTime \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Id": 906,
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e ",
                "InstanceId": "ins-ddada",
                "MachineName": "销售许可测试机器",
                "Status": 1,
                "Disks": "disk-dddd|ddd-test_系统盘",
                "CreateTime": "2024-09-19 21:46:09",
                "BackupTime": "2024-09-19 00:00:00",
                "ModifyTime": "2024-09-19 21:46:21",
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionCode": "gz",
                    "RegionId": 1,
                    "RegionName": "华南地区（广州）",
                    "RegionNameEn": "South China (Guangzhou)"
                }
            }
        ],
        "RequestId": "1703764f-b3ea-4d7f-99cb-cc3a6a62e2ec"
    }
}
```

