**Example 1: 获取任务类型属性**

获取任务类型属性

Input: 

```
tccli wedata GetWorkflowTaskTypeProperty --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskTypePropertyId db4b5ad4-005f-4f5d-8668-49a74981218c
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsRequestProperty": true,
            "IsResponseProperty": true,
            "PropertyDesc": "eyJlbi1VUyI6ICI0OiBDT1MiLCAiemgtQ04iOiAiNDpDT1MifQ==",
            "PropertyDescCn": "4:COS",
            "PropertyDescEn": "4: COS",
            "PropertyKey": "Source1",
            "PropertyName": "eyJlbi1VUyI6ICJTb3VyY2UiLCAiemgtQ04iOiAi5p2l5rqQIn0=",
            "PropertyNameCn": "来源",
            "PropertyNameEn": "Source",
            "PropertyValueUiDesc": "eyJlbi1VUyI6eyJyZW5kZXJIaWRkZW4iOnRydWUsImRlZmF1bHRWYWx1ZSI6IjQifSwiemgtQ04iOnsicmVuZGVySGlkZGVuIjp0cnVlLCJkZWZhdWx0VmFsdWUiOiI0In19",
            "PropertyValueUiType": "INPUT",
            "RequestValueRequired": 1,
            "TaskTypeName": "DATA_INTEGRATION",
            "TaskTypePropertyId": "db4b5ad4-005f-4f5d-8668-49a74981218c"
        },
        "RequestId": "fb3b564a-c8ad-4fe7-bc96-98ea5ca922c2"
    }
}
```

