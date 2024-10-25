**Example 1: 查询主机快照备份列表**

查询主机快照备份列表

Input: 

```
tccli cwp DescribeRansomDefenseBackupList --cli-unfold-argument  \
    --Order ASC \
    --Limit 1 \
    --Quuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --Offset 1 \
    --By CreateTime
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "BackupTime": "2024-10-21 00:00:00",
                "EventStatus": 0,
                "BackupStatus": 1,
                "Disks": "disk-2wnc|adaqlu-test_系统盘",
                "DiskCount": 1,
                "SnapshotIds": "snap-gbz1cigr",
                "StrategyId": 5570,
                "StrategyStatus": 1,
                "StrategyName": "tt1"
            }
        ],
        "RequestId": "9dae49e7-472a-9c0d-d5c4-e4a4ad9b4e8c"
    }
}
```

