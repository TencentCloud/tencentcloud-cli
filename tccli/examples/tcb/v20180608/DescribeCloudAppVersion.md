**Example 1: 查询云应用信息**



Input: 

```
tccli tcb DescribeCloudAppVersion --cli-unfold-argument  \
    --EnvId lowcode-**************** \
    --ServiceName html \
    --DeployType static-hosting \
    --VersionName html-002
```

Output: 
```
{
    "Response": {
        "BuildId": "2*********",
        "BuildTime": "2026-07-29 15:13:36",
        "BuildType": "ZIP",
        "Framework": "other",
        "StaticConfig": {
            "AppPath": "/html",
            "BuildPath": "",
            "CodeBranch": "",
            "CodeRepo": "",
            "CodeSource": "",
            "CosSuffix": "zip",
            "CosTimestamp": "1*********",
            "Framework": "other",
            "NodeJsVersion": "18",
            "StaticCmd": {
                "BuildCmd": "",
                "DeployCmd": "tcb hosting deploy ./ /html",
                "InstallCmd": ""
            },
            "StaticEnv": {
                "Variables": null
            },
            "ZipFileUrl": ""
        },
        "Status": "FAILED",
        "Steps": null,
        "RequestId": "b47866f0-2863-4721-818a-34a6ecd37cf7"
    }
}
```

