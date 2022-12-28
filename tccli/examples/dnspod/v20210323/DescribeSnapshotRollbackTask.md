**Example 1: 查询最近一次回滚**

 

Input: 

```
tccli dnspod DescribeSnapshotRollbackTask --cli-unfold-argument  \
    --Domain domain.com
```

Output: 
```
{
    "Response": {
        "RequestId": "fa4e8fe3-0a47-41e8-80d2-6833a1186286",
        "TaskId": 179,
        "SnapshotId": "A4EEXXXX",
        "CreatedOn": "2022-10-27 17:34:16",
        "Status": "ok",
        "Domain": "domain.com",
        "RecordCount": 65
    }
}
```

