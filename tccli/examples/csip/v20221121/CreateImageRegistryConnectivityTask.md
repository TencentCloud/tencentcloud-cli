**Example 1: 创建镜像仓库联通性检查任务**



Input: 

```
tccli csip CreateImageRegistryConnectivityTask --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --RegistryName 测试镜像仓库 \
    --RegistryRegion ap-guangzhou \
    --RegistryType tcr \
    --ApiVersion 1.0 \
    --UserName default-user \
    --Password default-password \
    --Url ccr.ccs.tencentyun.com \
    --Params.0.InstanceUuid backend \
    --Params.0.Region ap-guangzhou \
    --Params.0.Quuid backend
```

Output: 
```
{
    "Response": {
        "TaskId": "5a19ab3b-66a0-4f57-bad9-72c5cc17fc2f",
        "RequestId": "317f9a9e-7db9-4955-ba70-3f558e479f11"
    }
}
```

