**Example 1: 删除项目环境变量**



Input: 

```
tccli makers DeleteProjectEnvs --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --EnvVars.0.Key CAPI_TEST \
    --EnvVars.0.Value 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b993a11a-ec2b-4dcb-aa17-8adb9ebbcb6e"
    }
}
```

