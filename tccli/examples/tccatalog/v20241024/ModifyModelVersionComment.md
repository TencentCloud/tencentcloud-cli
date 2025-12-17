**Example 1: 测试**



Input: 

```
tccli tccatalog ModifyModelVersionComment --cli-unfold-argument  \
    --CatalogName testcatalog \
    --SchemaName testschema \
    --ModelName testmodel \
    --ModelVersion 1.0.0 \
    --NewComment comment
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "ModelVersion": {}
    }
}
```

