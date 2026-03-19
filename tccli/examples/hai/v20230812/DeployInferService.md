**Example 1: DeployInferService**



Input: 

```
tccli hai DeployInferService --cli-unfold-argument  \
    --ServiceMetaData.ServiceName hai-infer \
    --ServiceMetaData.ServiceChargeType POSTPAID_BY_HOUR \
    --ComputeInfo.ComputeResources.0.BundleType 96G_A*1 \
    --ComputeInfo.ComputeResources.0.Count 1 \
    --ComputeInfo.Replicas 1 \
    --DeploymentConfigs.0.Container.Image.ImageRegistryUrl aicompute.tencentcloudcr.com/aibench/sglang:v0.5.2rc2-hml-mooncake-0.3.6 \
    --DeploymentConfigs.0.Container.Port 30000 \
    --DeploymentConfigs.0.Container.Scripts bash \
    --DeploymentConfigs.0.Container.Envs.0.Name MODEL_DIRECTORY \
    --DeploymentConfigs.0.Container.Envs.0.Value /hai/model \
    --DeploymentConfigs.0.Container.Storages.0.MountPath /hai/model \
    --DeploymentConfigs.0.Container.Storages.0.COSStorage.URI cos://hai-model-bj-1319662662/Qwen3-Embedding-8B \
    --DeploymentConfigs.0.ContainerCount 1
```

Output: 
```
{
    "Response": {
        "ServiceId": "svc-8iia9ryo",
        "RequestId": "ced0e2a2-36e4-49fa-b86b-542befeb3629"
    }
}
```

