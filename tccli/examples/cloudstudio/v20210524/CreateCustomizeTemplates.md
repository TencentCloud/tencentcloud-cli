**Example 1: CreateCustomizeTemplates**



Input: 

```
tccli cloudstudio CreateCustomizeTemplates --cli-unfold-argument  \
    --UserDefinedTemplateParams.Source pmtoue \
    --UserDefinedTemplateParams.Icon https://cs-res.codehub.cn/vscode/go.svg \
    --UserDefinedTemplateParams.Name test-template-123 \
    --UserDefinedTemplateParams.Description Go1.16.7 \
    --UserDefinedTemplateParams.Tags Go \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 39,
            "Category": "userDefined",
            "Name": "test-template-123",
            "Description": "Go1.16.7",
            "DescriptionEN": "Go1.16.7",
            "Tags": "Go",
            "Icon": "https://cs-res.codehub.cn/vscode/go.svg",
            "VersionControlType": "CUSTOM",
            "VersionControlUrl": "",
            "VersionControlDesc": null,
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
            "CreateDate": "2022-06-15T11:52:25.221Z",
            "LastModified": "2022-06-15T11:52:25.221Z",
            "Sort": 0,
            "SnapshotUid": "HRFOYcbwNR",
            "UserId": 27,
            "Author": "frankzyfeng_test",
            "Me": true,
            "AuthorAvatar": null
        },
        "RequestId": "cf457d4a-bc75-477c-b2ad-dc02779d798c"
    }
}
```

