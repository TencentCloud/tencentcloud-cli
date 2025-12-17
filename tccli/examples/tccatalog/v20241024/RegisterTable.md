**Example 1: 示例一**

示例一

Input: 

```
tccli tccatalog RegisterTable --cli-unfold-argument  \
    --CatalogName t4 \
    --SchemaName dv \
    --TableName tv \
    --TableFormat ICEBERG \
    --MetadataLocation drv
```

Output: 
```
{
    "Response": {
        "SessionId": "17fb0e85-6b2c-4936-87c0-19b63ec19f5d-SIMPLE-root-t4",
        "RequestId": "e300b45a-81c5-4ba8-8dd9-c4e42fa0090e"
    }
}
```

