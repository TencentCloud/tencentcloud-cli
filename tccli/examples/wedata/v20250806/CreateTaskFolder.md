**Example 1: 创建任务文件夹**



Input: 

```
tccli wedata CreateTaskFolder --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --ParentTaskFolderPath / \
    --TaskFolderName tf_251113_225934 \
    --TaskFolderType ETL \
    --WorkflowId ca0f324e-6a45-4da2-9332-174222c6162a
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskFolderId": "17c01d1a-2e58-4353-9f61-d3558baddd52"
        },
        "RequestId": "1392190b-34de-4c42-8a8d-39e7fe06b6c8"
    }
}
```

