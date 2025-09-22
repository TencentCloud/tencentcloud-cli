**Example 1: 获取sql目录列表示例**



Input: 

```
tccli wedata ListSQLFolderContents --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --ParentFolderPath /abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessScope": "SHARED",
                "Children": [],
                "CreateUserUin": "100041136798",
                "Id": "c687e090-af62-44dc-878b-120dfa116216",
                "IsLeaf": false,
                "Name": null,
                "NodePermission": null,
                "OwnerUin": "100041136798",
                "Params": "",
                "ParentFolderPath": null,
                "Path": "/abc/2u7ea7u6539u540d01",
                "Type": "folder"
            }
        ],
        "RequestId": "3379217c-76da-4b00-a6ff-738f4959d184"
    }
}
```

