**Example 1: Modifying table remarks**

This example shows you how to modify table remarks.

Input: 

```
tccli tcaplusdb ModifyTableMemos --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableMemos.0.TableInstanceId tcaplus-1f224454 \
    --TableMemos.0.TableGroupId 101 \
    --TableMemos.0.TableName tb_example \
    --TableMemos.0.Memo 'pb test table 1xx'
```

Output: 
```
{
    "Response": {
        "RequestId": "c3446e81-4d07-4a80-a07f-f34f94b598bc",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": "PROTO",
                "TaskId": null,
                "TaskIds": null
            }
        ],
        "TotalCount": 1
    }
}
```

