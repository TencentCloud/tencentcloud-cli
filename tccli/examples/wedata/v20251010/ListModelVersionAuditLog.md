**Example 1: 查询模型版本活动列表**

查询模型版本活动列表

Input: 

```
tccli wedata ListModelVersionAuditLog --cli-unfold-argument  \
    --CatalogName test_model_catalog \
    --SchemaName test_schema_catalog \
    --ModelName experiment_with_tag1 \
    --PageNumber 1 \
    --PageSize 10 \
    --WorkspaceId 17663856806379896
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "OperationObject": "1",
                    "OperationObjectType": "MODEL_VERSION",
                    "OperationTime": "1767781406993",
                    "OperationType": "CREATE_MODEL_VERSION",
                    "Operator": "700002164618",
                    "OperatorName": "wedata30-dev@tencent.com"
                }
            ],
            "PageCount": "1",
            "PageNumber": "1",
            "PageSize": "10",
            "TotalCount": "1"
        },
        "RequestId": "d045b0ca-4b68-4806-9ca6-5360279eee93"
    }
}
```

