**Example 1: DescribeWorkspaceStatus**



Input: 

```
tccli cloudstudio DescribeWorkspaceStatus --cli-unfold-argument  \
    --CloudStudioSessionTeam cloudstudio-devops \
    --SpaceKey ryvzki
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 9,
            "Name": "open_api_test-1",
            "Owner": {
                "Id": 8,
                "AuthenticationUserInfo": {
                    "Team": "qcloud",
                    "UserName": "600000560939",
                    "NickName": "frankzyfeng@tencent.com",
                    "IsAdmin": false,
                    "IsTrial": null
                },
                "Avatar": null,
                "Features": null,
                "PreviewStatus": 0
            },
            "SpaceKey": "ryvzki",
            "Status": "CREATING",
            "LastOpsDate": "2022-06-10T06:55:45Z",
            "Description": "",
            "Share": {
                "Status": false,
                "WithMe": false,
                "BeginDate": null,
                "EndDate": null,
                "Users": []
            },
            "WorkspaceType": "NORMAL",
            "Label": "支持 Java、Go、Python 等多种语言",
            "WorkspaceVersion": 3,
            "ImageIcon": "https://cs-res.codehub.cn/workspace/assets/icons/all-in-one.svg",
            "CreateDate": "2022-06-10T06:55:45Z",
            "VersionControlUrl": "",
            "VersionControlDesc": null,
            "VersionControlRef": null,
            "VersionControlRefType": null,
            "VersionControlType": "GIT",
            "TemplateId": null,
            "SnapshotUid": null,
            "SpecDesc": null,
            "Cpu": 0,
            "Memory": 0
        },
        "RequestId": "9313fef5-5c9e-4b9b-ba09-411b11e4f7af"
    }
}
```

