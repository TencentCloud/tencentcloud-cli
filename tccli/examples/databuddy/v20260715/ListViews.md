**Example 1: 获取view列表**

获取view列表

Input: 

```
tccli databuddy ListViews --cli-unfold-argument  \
    --CatalogName s***a*0710 \
    --SchemaName information_schema \
    --MaxResults 100 \
    --WorkspaceId 17836526087487468
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AssetGuid": "tcc***l*g.v1.uid32789*23*359412846*@**00734**_ap-*ua*gzhou_VIEW",
                    "Audit": {
                        "CreatedAt": "1783652632924",
                        "Creator": "70000*1***1*",
                        "CreatorName": "**dat**0******@tencent.com",
                        "LastModifiedAt": "1783652640433",
                        "LastModifier": "700*0**64***",
                        "LastModifierName": "*e*ata30*****1@tencent.com"
                    },
                    "Columns": [
                        {
                            "Comment": "metalake name",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "metalake_name",
                            "Tags": [],
                            "Type": "string"
                        }
                    ],
                    "Comment": "catalog_privileges",
                    "MetaOwner": {
                        "FullName": "svmgao0710.information_schema.catalog_privileges",
                        "Owner": "700*0*1*4*1*",
                        "OwnerName": "***********st1@tencent.com",
                        "OwnerType": "user"
                    },
                    "Name": "catalog_privileges",
                    "Properties": [
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid3278902383594128462"
                        }
                    ],
                    "Tags": []
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "20704381-273a-431f-bc1d-ecaa5923314f"
    }
}
```

