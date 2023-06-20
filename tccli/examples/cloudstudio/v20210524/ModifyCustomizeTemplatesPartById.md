**Example 1: ModifyCustomizeTemplatesPartById**



Input: 

```
tccli cloudstudio ModifyCustomizeTemplatesPartById --cli-unfold-argument  \
    --UserDefinedTemplatePatchedParams.Source yueuli \
    --UserDefinedTemplatePatchedParams.Name test-case-2 \
    --Id 38 \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 38,
            "Category": "userDefined",
            "Name": "test-case-2",
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
            "LastModified": "2022-06-15T07:53:29.081Z",
            "Sort": 0,
            "SnapshotUid": "H8fDAMSDKU",
            "UserId": 27,
            "Author": "frankzyfeng_test",
            "Me": true,
            "AuthorAvatar": null
        },
        "RequestId": "7f02e8bc-48ac-4af0-9a0e-20e94715945a"
    }
}
```

