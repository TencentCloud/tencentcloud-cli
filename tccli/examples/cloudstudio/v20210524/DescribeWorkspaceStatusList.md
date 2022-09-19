**Example 1: DescribeWorkspaceStatusList**



Input: 

```
tccli cloudstudio DescribeWorkspaceStatusList --cli-unfold-argument  \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": [
            {
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
            {
                "Id": 8,
                "Name": "open_api_test5",
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
                "SpaceKey": "wvqlyf",
                "Status": "CREATING",
                "LastOpsDate": "2022-06-10T04:21:56Z",
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
                "CreateDate": "2022-06-10T04:21:56Z",
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
            }
        ],
        "RequestId": "ff57bfab-60d0-47ce-883c-f5230245636a"
    }
}
```

