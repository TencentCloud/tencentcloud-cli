**Example 1: 查询函数列表**

查询函数列表

Input: 

```
tccli wedata ListFunctions --cli-unfold-argument  \
    --CatalogName tsing_catalog \
    --SchemaName tsing_schema1 \
    --MaxResults 1 \
    --PageToken eyJvZmZzZXQiOjF9 \
    --WorkspaceId 17678671667189298
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.uid2107507754533063173@260073493_ap-guangzhou_FUNCTION",
                    "Audit": {
                        "CreatedAt": "1770105674338",
                        "Creator": "700002164619",
                        "CreatorName": "wedata30-test1@tencent.com",
                        "LastModifiedAt": "1770366444572",
                        "LastModifier": "700002164619",
                        "LastModifierName": "wedata30-test1@tencent.com"
                    },
                    "ClassName": "com.example.udf.ExampleUDF",
                    "Comment": "函数f2",
                    "EngineType": "spark",
                    "FunctionType": "java",
                    "MetaOwner": {
                        "FullName": "tsing_catalog.tsing_schema1.f2",
                        "Owner": "700002164619",
                        "OwnerName": "wedata30-test1@tencent.com",
                        "OwnerType": "user"
                    },
                    "Name": "f2",
                    "Properties": [
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid2107507754533063173"
                        }
                    ],
                    "Resources": [
                        {
                            "ResourceType": "jar",
                            "Uri": "cos://bucket/path/udf.jar"
                        }
                    ]
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjJ9"
        },
        "RequestId": "7e5a1208-65fe-4ee8-9dc3-f29f31d6067b"
    }
}
```

