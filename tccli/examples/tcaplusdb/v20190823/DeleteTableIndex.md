**Example 1: 删除表格分布式索引**

删除表格分布式索引

Input: 

```
tccli tcaplusdb DeleteTableIndex --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "abc",
                "TaskId": "abc",
                "TableName": "abc",
                "TableType": "1",
                "TableIdlType": "1",
                "TableGroupId": "342324",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "234232"
                ],
                "ApplicationId": "2342"
            }
        ],
        "RequestId": "23424211"
    }
}
```

