**Example 1: 获取codestudio文件夹详情**



Input: 

```
tccli wedata GetCodeFolder --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --FolderId fa659130-3ea8-4332-bd2a-05d87d92c04a
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "Children": null,
            "CreateUserUin": "100029411056",
            "Id": "fa659130-3ea8-4332-bd2a-05d87d92c04a",
            "IsLeaf": false,
            "NodePermission": null,
            "OwnerUin": "100029411056",
            "Params": null,
            "Path": "/test2",
            "Title": "test2",
            "Type": "folder"
        },
        "RequestId": "d96fdf5f-c195-4fbd-b6a4-3bcaf4f15742"
    }
}
```

