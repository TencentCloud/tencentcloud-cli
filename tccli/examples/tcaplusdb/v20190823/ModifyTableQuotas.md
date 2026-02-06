**Example 1: 表格扩缩容**

表格扩缩容

Input: 

```
tccli tcaplusdb ModifyTableQuotas --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableQuotas.0.TableInstanceId tcaplus-1f224454 \
    --TableQuotas.0.TableGroupId 101 \
    --TableQuotas.0.TableName tb_example \
    --TableQuotas.0.TableIdlType PROTO \
    --TableQuotas.0.ReservedVolume 2 \
    --TableQuotas.0.ReservedReadQps 240 \
    --TableQuotas.0.ReservedWriteQps 78
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TableResults": [
            {
                "TableInstanceId": "tcaplus-1f224454",
                "TaskId": "12313",
                "TableName": "tb_example",
                "TableType": "2",
                "TableIdlType": "1",
                "TableGroupId": "3242",
                "Error": {
                    "Code": "",
                    "Message": ""
                },
                "TaskIds": [
                    "32525"
                ],
                "ApplicationId": "32252"
            }
        ],
        "RequestId": "1252232"
    }
}
```

