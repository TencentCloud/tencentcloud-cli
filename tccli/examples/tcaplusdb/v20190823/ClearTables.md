**Example 1: 清除表**

清除表

Input: 

```
tccli tcaplusdb ClearTables --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example
```

Output: 
```
{
    "Response": {
        "RequestId": "122bb375-7464-4536-a3c5-8ddbdd6f4ce4",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": "5674209986-1199",
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: clearTable**

clearTable-test

Input: 

```
tccli tcaplusdb ClearTables --cli-unfold-argument  \
    --ClusterId 19090249266 \
    --SelectedTables.0.TableGroupId 1 \
    --SelectedTables.0.TableName auto_proto2_gene_0_27110510 \
    --SelectedTables.0.TableIdlType TDR \
    --SelectedTables.0.TableType GENERIC
```

Output: 
```
{
    "Response": {
        "RequestId": "0488b016-9c9e-44d5-9bd1-55f8f59cc0d0",
        "TableResults": [
            {
                "ApplicationId": null,
                "Error": {
                    "Code": "MissingParameter",
                    "Message": "Missing parameter TableInstanceId"
                },
                "TableGroupId": null,
                "TableIdlType": null,
                "TableInstanceId": null,
                "TableName": null,
                "TableType": null,
                "TaskId": null,
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

