**Example 1: 列出任务类型属性**

列出任务类型属性

Input: 

```
tccli wedata ListWorkflowTaskTypeProperties --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskTypeName SQL
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowTaskTypePropertyList": [
                {
                    "IsRequestProperty": true,
                    "IsResponseProperty": true,
                    "PropertyDesc": "eyJlbi1VUyI6ICJEYXRhU291cmNlIElkIiwgInpoLUNOIjogIuaVsOaNrua6kElEIn0=",
                    "PropertyDescCn": "数据源ID",
                    "PropertyDescEn": "DataSource Id",
                    "PropertyKey": "DataSourceId",
                    "PropertyName": "eyJlbi1VUyI6ICJEYXRhU291cmNlIElkIiwgInpoLUNOIjogIuaVsOaNrua6kElEIn0=",
                    "PropertyNameCn": "数据源ID",
                    "PropertyNameEn": "DataSource Id",
                    "PropertyValueUiDesc": "eyJlbi1VUyI6eyJyZW5kZXJIaWRkZW4iOnRydWV9LCJ6aC1DTiI6eyJyZW5kZXJIaWRkZW4iOnRydWV9fQ==",
                    "PropertyValueUiType": "INPUT",
                    "RequestValueRequired": 0,
                    "TaskTypeName": "SQL",
                    "TaskTypePropertyId": "18fdbc24-4f33-4af7-adf2-f86c2a8c7f96"
                }
            ]
        },
        "RequestId": "fca60e92-23d8-4a98-a5bd-fd113d232284"
    }
}
```

