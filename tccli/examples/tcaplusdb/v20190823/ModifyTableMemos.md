**Example 1: 修改表备注信息**

修改表备注信息

Input: 

```
tccli tcaplusdb ModifyTableMemos --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableMemos.0.TableInstanceId tcaplus-1f224454 \
    --TableMemos.0.TableGroupId 101 \
    --TableMemos.0.TableName tb_example \
    --TableMemos.0.Memo pb测试表1xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "3753",
                "TaskId": "34643",
                "TableName": "tb_example",
                "TableType": "1",
                "TableIdlType": "2",
                "TableGroupId": "`1321",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "35235"
                ],
                "ApplicationId": "14512"
            }
        ],
        "RequestId": "164574"
    }
}
```

