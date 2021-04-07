**Example 1: 查询快照列表**

查询表的快照

Input: 

```
tccli tcaplusdb DescribeSnapshots --cli-unfold-argument  \
    --ClusterId 18685341856 \
    --TableGroupId 1 \
    --TableName cl_generic
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "SnapshotCreateTime": "2020-09-22 00:00:00",
                "TableGroupId": "1",
                "SnapshotSize": 1,
                "SnapshotName": "test",
                "SnapshotTime": "2020-09-22 00:00:00",
                "TableName": "cl_generic",
                "SnapshotStatus": 1,
                "TaskId": "xx",
                "Error": {
                    "Message": "xx",
                    "Code": "xx"
                },
                "SnapshotDeadTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

