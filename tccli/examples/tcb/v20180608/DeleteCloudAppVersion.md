**Example 1: 删除云应用版本**



Input: 

```
tccli tcb DeleteCloudAppVersion --cli-unfold-argument  \
    --EnvId env-xx12 \
    --DeployType static-hosting \
    --ServiceName vue \
    --VersionName vue-01
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "c4ab40c6-be31-4b3c-b70d-de920f28d262"
    }
}
```

