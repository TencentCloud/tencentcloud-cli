**Example 1: DescribeCustomizeTemplatesById**



Input: 

```
tccli cloudstudio DescribeCustomizeTemplatesById --cli-unfold-argument  \
    --Id 2 \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 2,
            "Category": "general",
            "Name": "Ubuntu 18.04",
            "Description": "内置 Python 2.7",
            "DescriptionEN": "内置 Python 2.7",
            "Tags": "Ubuntu,Python",
            "Icon": "https://cs-res.codehub.cn/vscode/default.svg",
            "VersionControlType": "GIT",
            "VersionControlUrl": "https://e.coding.net/coding-public/cloud-studio-samples/cpp-quickstart.git",
            "VersionControlDesc": "快速开始",
            "VersionControlOwner": "system",
            "VersionControlRef": null,
            "VersionControlRefType": null,
            "UserVersionControlUrl": null,
            "UserVersionControlType": null,
            "UserVersionControlRef": null,
            "UserVersionControlRefType": null,
            "DevFile": null,
            "PluginFile": null,
            "Marked": false,
            "MarkAt": 0,
            "CreateDate": "2022-06-07T23:49:53Z",
            "LastModified": "2022-06-07T23:49:53Z",
            "Sort": 98999,
            "SnapshotUid": null,
            "UserId": 0,
            "Author": null,
            "Me": false,
            "AuthorAvatar": null
        },
        "RequestId": "734551f9-1653-4dc2-a95e-9e20e266428e"
    }
}
```

