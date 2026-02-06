**Example 1: 删除任务文件夹**

删除任务文件夹

Input: 

```
tccli wedata DeleteTaskFolder --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --WorkflowId ca0f324e-6a45-4da2-9332-174222c6162a \
    --TaskFolderId 575cef14-af74-40ae-b90d-714ca018fb88
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "03f815af-7673-4769-a1bf-aa53796c6123"
    }
}
```

