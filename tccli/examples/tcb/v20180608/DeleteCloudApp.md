**Example 1: 删除云应用**



Input: 

```
tccli tcb DeleteCloudApp --cli-unfold-argument  \
    --EnvId env-xx12 \
    --DeployType static-hosting \
    --ServiceName vue
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "0c0f8ed3-dcb2-43cf-a3a1-9df779f2a0ec"
    }
}
```

