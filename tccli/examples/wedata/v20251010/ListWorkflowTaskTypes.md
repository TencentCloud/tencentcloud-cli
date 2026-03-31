**Example 1: 列出任务类型属性**

列出任务类型属性

Input: 

```
tccli wedata ListWorkflowTaskTypes --cli-unfold-argument  \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowTaskTypeList": [
                {
                    "DisplayTaskType": "eyJlbi1VUyI6ICJTUUwiLCAiemgtQ04iOiAiU1FMIn0=",
                    "ModuleType": "ONEFLOW",
                    "TaskTypeDesc": "eyJlbi1VUyI6ICJTUUwiLCAiemgtQ04iOiAiU1FMIn0=",
                    "TaskTypeId": "31675135-a7cc-48ce-b98d-683ce6dcf145",
                    "TaskTypeName": "SQL"
                }
            ]
        },
        "RequestId": "b5fac3b3-5606-46b8-a46e-05bf303417d4"
    }
}
```

