**Example 1: 表格扩缩容**

表格扩缩容

Input: 

```
tccli tcaplusdb ModifyTableQuotas --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableQuotas.0.TableIdlType PROTO \
    --TableQuotas.0.TableGroupId 101 \
    --TableQuotas.0.FileExtType xx \
    --TableQuotas.0.TableInstanceId tcaplus-1f224454 \
    --TableQuotas.0.Memo xx \
    --TableQuotas.0.TableName tb_example \
    --TableQuotas.0.ReservedReadQps 0 \
    --TableQuotas.0.ListElementNum 0 \
    --TableQuotas.0.ReservedVolume 0 \
    --TableQuotas.0.ReservedWriteQps 0 \
    --TableQuotas.0.FileSize 0 \
    --TableQuotas.0.FileContent xx \
    --TableQuotas.0.FileName xx \
    --TableQuotas.0.TableType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "bb90baab-4189-4d01-9e92-250b57c571b3",
        "TableResults": [
            {
                "Error": null,
                "TableGroupId": "101",
                "TableIdlType": null,
                "TableInstanceId": "tcaplus-1f224454",
                "TableName": "tb_example",
                "TableType": null,
                "TaskId": null,
                "TaskIds": [
                    "5674209986-1201",
                    "5674209986-1202"
                ]
            }
        ],
        "TotalCount": 1
    }
}
```

