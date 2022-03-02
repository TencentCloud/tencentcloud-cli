**Example 1: 查询集群的备份集**



Input: 

```
tccli tdcpg DescribeClusterBackups --cli-unfold-argument  \
    --ClusterId tdcpg-xx \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "BackupSet": [
            {
                "BackupDataSize": 10,
                "BackupDataTime": "2022-01-05T22:26:31+08:00",
                "BackupId": 288051,
                "BackupMethod": "AUTO",
                "BackupTaskEndTime": "2022-01-05T22:34:09+08:00",
                "BackupTaskStartTime": "2022-01-05T00:00:00+08:00",
                "BackupTaskStatus": "SUCCESS",
                "BackupType": "SNAPSHOT"
            }
        ],
        "RequestId": "e7ec1877-12b9-42b9-93b2-55041f0c1c5f",
        "TotalCount": 7
    }
}
```

