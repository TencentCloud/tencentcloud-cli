**Example 1: 获取已发布的CodeFile列表**

获取已发布的CodeFile列表

Input: 

```
tccli wedata ListReleasedCodeFile --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CodeFileConfig": {
                        "AdvanceConfig": "",
                        "DefaultCatalog": "",
                        "DefaultSchema": "",
                        "ExtraParams": "",
                        "Params": "e30=",
                        "ResourceId": ""
                    },
                    "CodeFileId": "796741809075576832",
                    "CodeFileName": "bonney_sql.sql",
                    "ExtensionType": "",
                    "NodePath": "",
                    "VersionId": "797117940053737472"
                }
            ],
            "PageNumber": 1,
            "PageSize": 5,
            "TotalCount": "5",
            "TotalPageNumber": "1"
        },
        "RequestId": "240c4031-adbc-485a-95f7-492426ba93c1"
    }
}
```

