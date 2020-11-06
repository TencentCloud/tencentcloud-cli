**Example 1: 添加实例到计算环境**



Input: 

```
tccli batch AttachInstances --cli-unfold-argument  \
    --EnvId env-nuydksjj \
    --Instances.0.InstanceId ins-dus5t7tu \
    --Instances.0.ImageId img-8toqc6s3 \
    --Instances.0.LoginSettings.Password xxxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "a402b86a-5b45-4edf-b64c-d233c2984fbd"
    }
}
```

