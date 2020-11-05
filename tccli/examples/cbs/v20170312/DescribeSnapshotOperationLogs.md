**Example 1: Querying Snapshot Operation Log**



Input: 

```
tccli cbs DescribeSnapshotOperationLogs --cli-unfold-argument  \
    --Filters.0.Name snapshot-id\
    --Filters.0.Values snap-0y61iiyj
```

Output: 
```
{
    "Response": {
        "SnapshotOperationLogSet": [
            {
                "OperationState": "SUCCESS",
                "StartTime": "2018-12-18 17:52:37",
                "Operator": "546816713",
                "SnapshotId": "snap-0y61iiyj",
                "Operation": "SNAP_OPERATION_ROLLBACK",
                "EndTime": "2018-12-18 17:52:38"
            },
            {
                "OperationState": "SUCCESS",
                "StartTime": "2018-12-18 17:51:47",
                "Operator": "546816713",
                "SnapshotId": "snap-0y61iiyj",
                "Operation": "SNAP_OPERATION_ROLLBACK",
                "EndTime": "2018-12-18 17:51:48"
            },
            {
                "OperationState": "SUCCESS",
                "StartTime": "2018-12-18 11:57:46",
                "Operator": "",
                "SnapshotId": "snap-0y61iiyj",
                "Operation": "ASP_OPERATION_CREATE_SNAP",
                "EndTime": "2018-12-18 11:57:47"
            }
        ],
        "RequestId": "0dc7b07a-5f6b-46c4-b1d9-048e37d1c33c"
    }
}
```

