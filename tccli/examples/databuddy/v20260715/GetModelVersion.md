**Example 1: 获取模型版本详情**



Input: 

```
tccli databuddy GetModelVersion --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ModelName my_model \
    --ModelVersion 1 \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "ModelVersion": {
                "Version": "1",
                "Uri": "cos://my-bucket/model/v1"
            }
        }
    }
}
```

