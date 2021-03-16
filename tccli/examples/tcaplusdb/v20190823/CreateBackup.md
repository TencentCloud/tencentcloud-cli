**Example 1: 创建备份**

创建备份

Input: 

```
tccli tcaplusdb CreateBackup --cli-unfold-argument  \
    --Remark test \
    --ClusterId 22762983670 \
    --SelectedTables.0.TableIdlType xx \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.FileExtType xx \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.Memo xx \
    --SelectedTables.0.TableName tb_example \
    --SelectedTables.0.ReservedReadQps 0 \
    --SelectedTables.0.ListElementNum 0 \
    --SelectedTables.0.ReservedVolume 0 \
    --SelectedTables.0.ReservedWriteQps 0 \
    --SelectedTables.0.FileSize 0 \
    --SelectedTables.0.FileContent xx \
    --SelectedTables.0.FileName xx \
    --SelectedTables.0.TableType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "c3446e81-4d07-4a80-a07f-f34f94b598bc",
        "TaskIds": [
            "22762983670-1"
        ]
    }
}
```

