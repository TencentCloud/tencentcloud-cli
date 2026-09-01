**Example 1: 创建 custom 服务**



Input: 

```
tccli tcb CreateCloudApp --cli-unfold-argument  \
    --EnvId lowcode-**************** \
    --ServiceName my-vue-app-01 \
    --DeployType custom \
    --Source.Type git \
    --Source.Repo https://gi**u*********************-**********.git \
    --Source.Ref master \
    --Source.Channel github \
    --CustomSteps.0.Name ls \
    --CustomSteps.0.Command node -v \
    --NodeJsVersion 22
```

Output: 
```
{
    "Response": {
        "BuildId": "**********",
        "ServiceName": "my-***-***-**",
        "VersionName": "my-vue-app-01-001",
        "RequestId": "75628170-c5b9-4bda-b370-fec9dd4362f0"
    }
}
```

