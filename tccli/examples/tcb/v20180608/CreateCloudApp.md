**Example 1: 创建云应用**



Input: 

```
tccli tcb CreateCloudApp --cli-unfold-argument  \
    --EnvId lowcode-*********f985f96 \
    --ServiceName html \
    --DeployType static-hosting \
    --BuildType ZIP \
    --StaticConfig.Framework other \
    --StaticConfig.NodeJsVersion 18 \
    --StaticConfig.AppPath /html \
    --StaticConfig.CosTimestamp 17****9**5 \
    --StaticConfig.CosSuffix zip \
    --StaticConfig.StaticCmd.DeployCmd tcb hosting deploy ./ /html
```

Output: 
```
{
    "Response": {
        "BuildId": "26014**8*2",
        "ServiceName": "html",
        "VersionName": "html-002",
        "RequestId": "ba0e079a-c85d-43ec-a313-7e88f251646c"
    }
}
```

