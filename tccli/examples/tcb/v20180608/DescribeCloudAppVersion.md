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
        "RequestId": "b47866f0-2863-4721-818a-34a6ecd37cf7",
        "VersionDomain": "cl*u*ap*-****************************************************************",
        "Snapshot": "{\"Source\":{\"Type\":\"zip\",\"Repo\":\"\",\"Ref\":\"\",\"Commit\":\"\",\"PackageFileName\":\"\"},\"TriggerType\":\"manual\",\"Steps\":[{\"Name\":\"build-image\",\"Command\":\"D=/tmp/ctx-probe; curl -fsSL \\\"$ZIP_FILE_URL\\\" -o /tmp/c.zip \\u0026\\u0026 mkdir -p $D \\u0026\\u0026 unzip -o -q /tmp/c.zip -d $D \\u0026\\u0026 ls -la $D \\u0026\\u0026 tar -C $D -cf - . | docker build --platform linux/amd64 -t \\\"$CLOUDBASE_IMAGE_URL\\\" -\"},{\"Name\":\"push-image\",\"Command\":\"printf '%s' \\\"$CLOUDBASE_TCR_PASSWORD\\\" | docker login -u \\\"$CLOUDBASE_TCR_USERNAME\\\" --password-stdin \\\"$CLOUDBASE_TCR_REGISTRY\\\" \\u0026\\u0026 docker push \\\"$CLOUDBASE_IMAGE_URL\\\"\"}],\"ServiceList\":[],\"Env\":[]}"
    }
}
```

