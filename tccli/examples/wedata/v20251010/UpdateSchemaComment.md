**Example 1: 更新schema描述**

更新schema描述

Input: 

```
tccli wedata UpdateSchemaComment --cli-unfold-argument  \
    --CatalogName easechen_model_catalog_test \
    --SchemaName easechen_model_schema_test \
    --NewComment update schema comment
```

Output: 
```
{
    "Response": {
        "RequestId": "f731bc8e-7338-4b59-9e73-cead05669a05",
        "Data": {
            "Schema": {
                "Audit": {
                    "CreatedAt": "1760440757860",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "1761707838625",
                    "LastModifier": "1290245077@qq.com"
                },
                "Comment": "update schema comment",
                "Name": "easechen_model_schema_test",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid2382266867620974132"
                    }
                ]
            }
        }
    }
}
```

