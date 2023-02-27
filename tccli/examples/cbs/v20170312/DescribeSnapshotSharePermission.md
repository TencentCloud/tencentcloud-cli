**Example 1: 查询某个快照的分享信息**

查询某个快照的分享信息

Input: 

```
tccli cbs DescribeSnapshotSharePermission --cli-unfold-argument  \
    --SnapshotId snap-asxafa65
```

Output: 
```
{
    "Response": {
        "RequestId": "4ab150b9-538d-48fb-8821-7fa185f1d07c",
        "SharePermissionSet": [
            {
                "CreatedTime": "2019-07-08 00:00:06",
                "AccountId": "123456789"
            }
        ]
    }
}
```

