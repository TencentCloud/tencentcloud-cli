**Example 1: 获取schema列表**

获取schema列表

Input: 

```
tccli databuddy ListSchemas --cli-unfold-argument  \
    --CatalogName capi_no_delete_table \
    --MaxResults 1 \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tccatalog.v1.uid1482527818963963288@251436191_ap-guangzhou_SCHEMA",
                    "Audit": {
                        "CreatedAt": "1778825400056",
                        "Creator": "700002164618",
                        "CreatorName": "wedata30-dev@tencent.com",
                        "LastModifiedAt": "1778825400056",
                        "LastModifier": "700002164618",
                        "LastModifierName": "wedata30-dev@tencent.com"
                    },
                    "Comment": "",
                    "MetaOwner": {
                        "FullName": "capi_no_delete_table.capi_no_delete_schema",
                        "Owner": "700002164618",
                        "OwnerName": "wedata30-dev@tencent.com",
                        "OwnerType": "user"
                    },
                    "Name": "capi_no_delete_schema",
                    "Properties": [
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid1482527818963963288"
                        }
                    ],
                    "Tags": []
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "47d6c662-1c46-4227-bb34-6dc5db95b6a9"
    }
}
```

