**Example 1: 修改副本数**



Input: 

```
tccli hai UpdateServiceConfigs --cli-unfold-argument  \
    --ServiceId svc-b0t60zrw \
    --TargetReplicas 2
```

Output: 
```
{
    "Response": {
        "RequestId": "6b9561e7-7aa8-4e65-9870-2dc6db8014a0"
    }
}
```

**Example 2: 更新环境变量**



Input: 

```
tccli hai UpdateServiceConfigs --cli-unfold-argument  \
    --ServiceId svc-b0t60zrw \
    --DeploymentConfigs.0.Container.Image.ImageRegistryUrl aicompute.tencentcloudcr.com/aibench/sglang:v0.5.3rc0-hml-mooncake-0.3.6 \
    --DeploymentConfigs.0.Container.Port 30000 \
    --DeploymentConfigs.0.Container.Envs.0.Name TEST \
    --DeploymentConfigs.0.Container.Envs.0.Value UPDATED_ENV
```

Output: 
```
{
    "Response": {
        "RequestId": "b5a0d6fb-a235-4dc4-a888-0a219eb88d4b"
    }
}
```

