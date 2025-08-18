**Example 1: 修改表结构**

修改表结构

Input: 

```
tccli tcaplusdb ModifyTables --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --IdlFiles.0.FileName tb_example_modify \
    --IdlFiles.0.FileType PROTO \
    --IdlFiles.0.FileExtType proto \
    --IdlFiles.0.FileSize 292 \
    --IdlFiles.0.FileId 600 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.TableIdlType PROTO
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "123123",
                "TaskId": "43452",
                "TableName": "tb_example_modify",
                "TableType": "1",
                "TableIdlType": "1",
                "TableGroupId": "22141",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "321512"
                ],
                "ApplicationId": "421325"
            }
        ],
        "RequestId": "1254521"
    }
}
```

