**Example 1: DescribeCustomizeTemplates**



Input: 

```
tccli cloudstudio DescribeCustomizeTemplates --cli-unfold-argument  \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 1,
                "Category": "general",
                "Name": "All in One",
                "Description": "支持 Java、Go、Python 等多种语言",
                "DescriptionEN": "支持 Java、Go、Python 等多种语言",
                "Tags": "Java,Go,Python,Node.js",
                "Icon": "https://cs-res.codehub.cn/workspace/assets/icons/all-in-one.svg",
                "VersionControlType": "NONE",
                "VersionControlUrl": "",
                "VersionControlDesc": "",
                "VersionControlOwner": "system",
                "VersionControlRef": null,
                "VersionControlRefType": null,
                "UserVersionControlUrl": null,
                "UserVersionControlType": "NONE",
                "UserVersionControlRef": null,
                "UserVersionControlRefType": null,
                "DevFile": null,
                "PluginFile": null,
                "Marked": false,
                "MarkAt": 0,
                "CreateDate": "2022-06-07T23:49:53Z",
                "LastModified": "2022-06-07T23:49:53Z",
                "Sort": 99999,
                "SnapshotUid": null,
                "UserId": 0,
                "Author": null,
                "Me": false,
                "AuthorAvatar": null
            }
        ],
        "RequestId": "e7e64332-1419-4951-acf5-10dd886c96ee"
    }
}
```

