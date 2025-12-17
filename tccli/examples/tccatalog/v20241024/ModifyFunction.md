**Example 1: ModifyFunction示例**



Input: 

```
tccli tccatalog ModifyFunction --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1 \
    --FunctionName f1 \
    --NewClassName com.example.f1 \
    --NewResources.0.ResourceType file \
    --NewResources.0.Uri cosn://test-123446/f1.jar
```

Output: 
```
{
    "Response": {
        "Function": {
            "Audit": {
                "CreatedAt": 1760675682118,
                "CreatedTime": "2025-10-17 12:34:42",
                "Creator": "tccatalogK5@rZl.com",
                "LastModifiedAt": 1762485241764,
                "LastModifiedTime": "2025-11-07 11:14:01",
                "LastModifier": "tccatalogK5@rZl.com"
            },
            "ClassName": "com.example.f1",
            "EngineType": "spark",
            "FunctionType": "java",
            "Name": "f1",
            "Resources": [
                {
                    "ResourceType": "file",
                    "Uri": "cosn://test-123446/f1.jar"
                }
            ]
        },
        "RequestId": "8b01c65b-e092-4cbd-90d1-6077dcfdf884"
    }
}
```

