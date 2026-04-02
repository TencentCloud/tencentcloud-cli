**Example 1: 查询schema详情**

查询schema详情

Input: 

```
tccli wedata GetSchema --cli-unfold-argument  \
    --CatalogName mico_test_1018 \
    --SchemaName mico_schema_1027
```

Output: 
```
{
    "Response": {
        "RequestId": "c38c8e21-b9f0-4d60-b8da-45e21b31d1d2",
        "Data": {
            "Schema": {
                "Audit": {
                    "CreatedAt": "1761627980744",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "0",
                    "LastModifier": ""
                },
                "Comment": "test create schema",
                "MetaOwner": {
                    "FullName": "mico_test_1018.mico_schema_1027",
                    "Owner": "1290245077@qq.com",
                    "OwnerType": "user"
                },
                "Name": "mico_schema_1027",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid1052210150648680833"
                    }
                ]
            }
        }
    }
}
```

