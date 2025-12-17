**Example 1: ModifyFunctionComment示例**



Input: 

```
tccli tccatalog ModifyFunctionComment --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --FunctionName f1 \
    --NewComment fafea
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
        "RequestId": "a111c9e6-909b-484e-b73d-2b126503c212"
    }
}
```

