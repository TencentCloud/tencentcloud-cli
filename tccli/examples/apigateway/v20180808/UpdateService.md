**Example 1: UpdateService**

本接口（UpdateService）用于从服务发布的环境中运行版本切换到特定版本。用户在使用 API 网关创建服务并发布服务到某个环境后，多因开发过程会产生多个版本，此时可调用本接口。

Input: 

```
tccli apigateway UpdateService --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --EnvironmentName test \
    --VersionName 202002161926124aa59df4-7198-4f7a-acc7-887ab7ee0215 \
    --UpdateDesc test
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "7787aa0e-be74-43c0-b6f6-7bf56995ce2d"
    }
}
```

