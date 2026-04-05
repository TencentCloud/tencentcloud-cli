**Example 1: 复制模型版本**



Input: 

```
tccli wedata CopyModelVersion --cli-unfold-argument  \
    --SourceName testcatalog.testschema.table \
    --SourceModelVersion 1 \
    --TargetName targetcatalog.targetschema.table \
    --WorkspaceId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CopyFrom": "testcatalog.testschema.table:1",
            "Created": true,
            "ModelName": "targetcatalog.targetschema.table",
            "ModelVersion": "1"
        },
        "RequestId": "8f5b989d-2bcf-47d8-95a5-f3c7cee75071"
    }
}
```

