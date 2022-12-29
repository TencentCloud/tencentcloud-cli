**Example 1: 查询快照回滚结果，进行中**

 

Input: 

```
tccli dnspod DescribeSnapshotRollbackResult --cli-unfold-argument  \
    --Domain domain.com \
    --TaskId 177
```

Output: 
```
{
    "Response": {
        "RequestId": "a7723f78-ff6f-43bc-89ee-bc225376276b",
        "TaskId": 177,
        "SnapshotId": "A45AXXXX",
        "Status": "waiting",
        "Domain": "domain.com",
        "Progress": 0,
        "LeftMinutes": 1,
        "Success": null,
        "Failed": null,
        "Total": null,
        "CosUrl": null,
        "FailedRecordList": null
    }
}
```

**Example 2: 查询快照回滚结果，已完成**

 

Input: 

```
tccli dnspod DescribeSnapshotRollbackResult --cli-unfold-argument  \
    --Domain domain.com \
    --TaskId 177
```

Output: 
```
{
    "Response": {
        "RequestId": "d4c4c0e9-ca5a-44a2-9d51-b0c64656b8bb",
        "TaskId": 177,
        "SnapshotId": "A45AXXXX",
        "Success": 63,
        "Failed": 0,
        "CosUrl": "https://newdnspod-1252120672.cos.ap-shanghai.myqcloud.com/snapshot_rollback_91724229_xxx.csv",
        "Status": "ok",
        "Progress": 100,
        "LeftMinutes": 0,
        "Total": 63,
        "Domain": "domain.com",
        "FailedRecordList": []
    }
}
```

