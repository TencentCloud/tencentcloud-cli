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
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "abc8989",
                "TaskId": "768786",
                "TableName": "abc",
                "TableType": "1",
                "TableIdlType": "1",
                "TableGroupId": "2321",
                "TaskIds": [
                    "abc"
                ],
                "ApplicationId": "abc"
            }
        ],
        "RequestId": "abc"
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
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "abc",
                "TaskId": "abc",
                "TableName": "abc",
                "TableType": "abc",
                "TableIdlType": "abc",
                "TableGroupId": "abc",
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                },
                "TaskIds": [
                    "abc"
                ],
                "ApplicationId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

