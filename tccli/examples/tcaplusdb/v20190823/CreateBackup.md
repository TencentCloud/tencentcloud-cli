**Example 1: 创建备份**

创建备份

Input: 

```
tccli tcaplusdb CreateBackup --cli-unfold-argument  \
    --ClusterId 22762983670 \
    --SelectedTables.0.TableInstanceId tcaplus-1f224454 \
    --SelectedTables.0.TableGroupId 101 \
    --SelectedTables.0.TableName tb_example \
    --Remark test
```

Output: 
```
{
    "Response": {
        "RequestId": "c3446e81-4d07-4a80-a07f-f34f94b598bc",
        "TaskIds": [
            "22762983670-1"
        ],
        "ApplicationIds": [
            "34324234"
        ]
    }
}
```

