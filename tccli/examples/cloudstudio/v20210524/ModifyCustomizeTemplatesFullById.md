**Example 1: ModifyCustomizeTemplatesFullById**



Input: 

```
tccli cloudstudio ModifyCustomizeTemplatesFullById --cli-unfold-argument  \
    --UserDefinedTemplateParams.Source yueuli \
    --UserDefinedTemplateParams.Icon https://cs-res.codehub.cn/vscode/go.svg \
    --UserDefinedTemplateParams.Name hanley_666 \
    --UserDefinedTemplateParams.Description aaaaaa \
    --UserDefinedTemplateParams.Tags GO \
    --CloudStudioSessionTeam cloudstudio-devops \
    --Id 38
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 38,
            "Category": "userDefined",
            "Name": "hanley_666",
            "Description": "aaaaaa",
            "DescriptionEN": "aaaaaa",
            "Tags": "GO",
            "Icon": "https://cs-res.codehub.cn/vscode/go.svg",
            "VersionControlType": "CUSTOM",
            "VersionControlUrl": "",
            "VersionControlDesc": "",
            "VersionControlOwner": "system",
            "VersionControlRef": "",
            "VersionControlRefType": null,
            "UserVersionControlUrl": null,
            "UserVersionControlType": null,
            "UserVersionControlRef": null,
            "UserVersionControlRefType": null,
            "DevFile": null,
            "PluginFile": null,
            "Marked": false,
            "MarkAt": 0,
            "CreateDate": "2022-06-15T07:51:05Z",
            "LastModified": "2022-06-15T07:52:45.585Z",
            "Sort": 0,
            "SnapshotUid": "H8fDAMSDKU",
            "UserId": 27,
            "Author": "frankzyfeng_test",
            "Me": true,
            "AuthorAvatar": null
        },
        "RequestId": "a9fea1de-fc85-4e87-afaf-89d390691ca2"
    }
}
```

