**Example 1: 查询备份信息详情**

通过该接口查询指定实例备份 ID 的备份信息。

Input: 

```
tccli redis DescribeBackupDetail --cli-unfold-argument  \
    --InstanceId crs-g9my5vt7 \
    --BackupId 154571841-1165701309-438602494
```

Output: 
```
{
    "Response": {
        "BackupId": "154571841-1165701309-438602494",
        "BackupSize": 528,
        "BackupType": "0",
        "EndTime": "2022-12-19 19:42:20",
        "InstanceType": 9,
        "Locked": 0,
        "MemSize": 2048,
        "Remark": "test005",
        "ReplicasNum": 1,
        "RequestId": "add15b91-8f3c-4ff3-ba52-7c64c9c435ba",
        "ShardNum": 3,
        "StartTime": "2022-12-19 19:41:42",
        "Status": 2
    }
}
```

