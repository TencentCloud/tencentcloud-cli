**Example 1: 示例1**



Input: 

```
tccli wedata DescribeResourceManagePathTrees --cli-unfold-argument  \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CosBucket": "000-zzz-1315051789",
                "CosRegion": "ap-guangzhou",
                "CreateTime": 1734680616000,
                "ExtraInfo": null,
                "FileExtensionType": null,
                "IsLeaf": true,
                "LocalPath": "/datastudio/resource/qq.txt",
                "Md5Value": "",
                "Name": "qq.txt",
                "OwnerName": "peanutzhu",
                "RemotePath": "/datastudio/resource/1470547050521227264/20241220154304869/qq.txt",
                "ResourceId": "689959e7-4472-4eef-a1cb-1e519f4f3079",
                "Size": 149,
                "UpdateTime": 1734680616000,
                "UpdateUser": null,
                "UpdateUserId": null
            }
        ],
        "RequestId": "f9c5735a-30cc-47df-9053-788a645b1f70"
    }
}
```

