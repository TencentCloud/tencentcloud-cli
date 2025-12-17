**Example 1: ModifyFunctionClassName示例**



Input: 

```
tccli tccatalog ModifyFunctionClassName --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --FunctionName f1 \
    --NewClassName sfasfsafe
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
        "RequestId": "4ade75f0-8646-4688-9035-e0ffe835cc12"
    }
}
```

