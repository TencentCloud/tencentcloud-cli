**Example 1: ModifyFunctionResources示例**



Input: 

```
tccli tccatalog ModifyFunctionResources --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --FunctionName f1 \
    --NewResources.0.ResourceType fsfa \
    --NewResources.0.Uri fasfaf
```

Output: 
```
{
    "Response": {
        "Function": {
            "ClassName": "",
            "EngineType": "",
            "FunctionType": "",
            "Name": "",
            "Resources": null
        },
        "RequestId": "5bcf0099-5c58-42f4-ac34-bd0ad96afa67"
    }
}
```

