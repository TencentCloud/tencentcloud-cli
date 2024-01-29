**Example 1: 示例1**



Input: 

```
tccli wedata DescribeResourceManagePathTrees --cli-unfold-argument  \
    --ProjectId 11719389319917035521
```

Output: 
```
{
    "Response": {
        "RequestId": "2fe0e0e3-9e79-49fb-872b-4c6a1abdc335",
        "Data": [
            {
                "Name": "jaydenjhu",
                "IsLeaf": false,
                "ResourceId": "e2a6dd6e-6372-4e4e-995c-e318958da175",
                "LocalPath": "/datastudio/resource/jaydenjhu",
                "RemotePath": "/datastudio/resource/1171938931991703552/jaydenjhu",
                "FileExtensionType": null,
                "Size": null,
                "Md5Value": null,
                "OwnerName": "fe",
                "UpdateUser": null,
                "UpdateUserId": null,
                "CreateTime": 1657704560000,
                "UpdateTime": 1657704560000,
                "CosBucket": null,
                "CosRegion": null,
                "ExtraInfo": null
            },
            {
                "Name": "1-201111193502.zip",
                "IsLeaf": true,
                "ResourceId": "03343a77-b586-4b78-8e3e-2f1c30ba273a",
                "LocalPath": "/datastudio/resource/jaydenjhu/1-201111193502.zip",
                "RemotePath": "/datastudio/resource/1171938931991703552/jaydenjhu/1-201111193502.zip",
                "FileExtensionType": "zip",
                "Size": 4015960,
                "Md5Value": null,
                "OwnerName": "fe",
                "UpdateUser": null,
                "UpdateUserId": null,
                "CreateTime": 1663299308000,
                "UpdateTime": 1663299308000,
                "CosBucket": "jaydenjhu-1257305158",
                "CosRegion": "ap-guangzhou",
                "ExtraInfo": null
            },
            {
                "Name": "cos_token_1.jar",
                "IsLeaf": true,
                "ResourceId": "bdf74f83-4f63-47d2-89b2-26c3c08b735f",
                "LocalPath": "/datastudio/resource/jaydenjhu/cos_token_1.jar",
                "RemotePath": "/datastudio/resource/1171938931991703552/jaydenjhu/cos_token_1.jar",
                "FileExtensionType": "jar",
                "Size": 4292177,
                "Md5Value": null,
                "OwnerName": "fe",
                "UpdateUser": null,
                "UpdateUserId": null,
                "CreateTime": 1660627885000,
                "UpdateTime": 1660630699000,
                "CosBucket": "jaydenjhu-1257305158",
                "CosRegion": "ap-guangzhou",
                "ExtraInfo": null
            },
            {
                "Name": "wedata-udf-1.0-SNAPSHOT.jar",
                "IsLeaf": true,
                "ResourceId": "32d46df4-5316-4758-9c6d-1a841d8d91f8",
                "LocalPath": "/datastudio/resource/jaydenjhu/wedata-udf-1.0-SNAPSHOT.jar",
                "RemotePath": "/datastudio/resource/1171938931991703552/jaydenjhu/wedata-udf-1.0-SNAPSHOT.jar",
                "FileExtensionType": "jar",
                "Size": 3167,
                "Md5Value": null,
                "OwnerName": "fe",
                "UpdateUser": null,
                "UpdateUserId": null,
                "CreateTime": 1657704602000,
                "UpdateTime": 1657704602000,
                "CosBucket": "jaydenjhu-1257305158",
                "CosRegion": "ap-guangzhou",
                "ExtraInfo": null
            }
        ]
    }
}
```

