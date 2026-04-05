**Example 1: 查询函数详情**

查询函数详情

Input: 

```
tccli wedata GetFunction --cli-unfold-argument  \
    --CatalogName tsing_catalog \
    --SchemaName tsing_schema1 \
    --FunctionName f2 \
    --WorkspaceId 17678671667189298
```

Output: 
```
{
    "Response": {
        "Data": {
            "Function": {
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
        },
        "RequestId": "57de11e9-ddd9-465d-a7ad-5eb97d3a08b1"
    }
}
```

