**Example 1: 查询任务文件夹详情**

查询任务文件夹详情

Input: 

```
tccli wedata GetTaskFolder --cli-unfold-argument  \
    --ProjectId 1486804694126882816 \
    --WorkflowId 1eb20625-48fa-44db-a9bd-0d203750285f \
    --TaskFolderId e96662ab-ac31-47ab-9028-49ba2922ba78
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateUserUin": "100028579876",
            "TaskFolderId": "e96662ab-ac31-47ab-9028-49ba2922ba78",
            "TaskFolderName": "tf_251113",
            "TaskFolderPath": "/tf_251113",
            "ParentTaskFolderPath": "",
            "ProjectId": "1486804694126882816",
            "TaskFolderType": "GENERAL",
            "WorkflowId": "1eb20625-48fa-44db-a9bd-0d203750285f"
        },
        "RequestId": "eac802c8-ace1-48a6-8483-0f65d33c8bef"
    }
}
```

