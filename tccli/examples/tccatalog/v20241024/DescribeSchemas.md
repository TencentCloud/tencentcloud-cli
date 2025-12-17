**Example 1: DescribeSchemas示例**



Input: 

```
tccli tccatalog DescribeSchemas --cli-unfold-argument  \
    --CatalogName layyu_c1 \
    --SchemaNames information_schema
```

Output: 
```
{
    "Response": {
        "Schemas": [
            {
                "Audit": {
                    "CreatedAt": 1761640008525,
                    "CreatedTime": "2025-10-28 16:26:48",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": null,
                    "LastModifiedTime": "",
                    "LastModifier": ""
                },
                "Comment": "System information schema",
                "Name": "information_schema",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid1756319776178284041"
                    }
                ]
            }
        ],
        "RequestId": "d461193d-0d00-4d2b-818c-819d2bbfc283"
    }
}
```

