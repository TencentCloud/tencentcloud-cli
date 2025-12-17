**Example 1: CreateFunction示例**



Input: 

```
tccli tccatalog CreateFunction --cli-unfold-argument  \
    --CatalogName layyu_c1 \
    --SchemaName s1 \
    --FunctionName f1 \
    --FunctionType JAVA \
    --EngineType SPARK \
    --ClassName com.example.Test \
    --Resources.0.ResourceType file \
    --Resources.0.Uri cosn://test-12345/example.jar
```

Output: 
```
{
    "Response": {
        "Function": {
            "Audit": {
                "CreatedAt": 1762413587956,
                "CreatedTime": "2025-11-06 15:19:47",
                "Creator": "tccatalogK5@rZl.com",
                "LastModifiedAt": null,
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "ClassName": "com.example.Test",
            "EngineType": "spark",
            "FunctionType": "java",
            "Name": "f1",
            "Resources": [
                {
                    "ResourceType": "file",
                    "Uri": "cosn://test-12345/example.jar"
                }
            ]
        },
        "RequestId": "7d87ad05-e322-425c-8c6a-030c478c7ee3"
    }
}
```

