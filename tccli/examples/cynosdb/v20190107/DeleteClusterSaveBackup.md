**Example 1: 删除保留备份**

Delete Cluster Save Backup

Input: 

```
tccli cynosdb DeleteClusterSaveBackup --cli-unfold-argument  \
    --ClusterId cynosdbmysql-0fs2nhc7 \
    --SaveBackupId 64142
```

Output: 
```
{
    "Response": {
        "RequestId": "be38b494-263a-45f7-b6f3-ecbd66ac75bb",
        "TaskId": 19297
    }
}
```

