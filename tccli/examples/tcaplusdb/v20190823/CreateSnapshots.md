**Example 1: 创建快照**



Input: 

```
tccli tcaplusdb CreateSnapshots --cli-unfold-argument  \
    --ClusterId xx \
    --SelectedTables.0.SnapshotName 666 \
    --SelectedTables.0.TableGroupId 1 \
    --SelectedTables.0.SnapshotTime 2020-09-22 00:00:00 \
    --SelectedTables.0.TableName cl_generic \
    --SelectedTables.0.SnapshotDeadTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "17af6a7a-1fcc-4c1d-a4a2-caab4d9e75cc",
        "TableResults": [
            {
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "SnapshotCreateTime": "2021-03-19 11:40:40",
                "SnapshotDeadTime": "2021-03-20 11:40:30",
                "SnapshotName": "666",
                "SnapshotSize": 0,
                "SnapshotStatus": 0,
                "SnapshotTime": "2021-03-12 11:40:32",
                "TableGroupId": "1",
                "TableName": "cl_generic",
                "TaskId": ""
            }
        ],
        "TotalCount": 1
    }
}
```

