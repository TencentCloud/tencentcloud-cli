**Example 1: ListCodeFolderContents**



Input: 

```
tccli wedata ListCodeFolderContents --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --ParentFolderPath / \
    --Keyword u76eeu5f55 \
    --OnlyFolderNode True \
    --OnlyUserSelfScript False
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessScope": "SHARED",
                "Children": [],
                "CreateUserUin": "100028579606",
                "Id": "cbcb6192-f047-49a3-9593-56f0e81ac900",
                "IsLeaf": false,
                "NodePermission": null,
                "OwnerUin": "100028579606",
                "Params": "",
                "Path": "/juno0829-1",
                "Title": "juno0829-1",
                "Type": "folder"
            }
        ],
        "RequestId": "637a9492-2aa7-40f0-b9a9-43cac3971375"
    }
}
```

