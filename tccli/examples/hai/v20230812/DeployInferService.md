**Example 1: DeployInferService**



Input: 

```
tccli hai DeployInferService --cli-unfold-argument  \
    --ServiceMetaData.ServiceName 外租_DeepSeek-R1-Distill-Qwen-7B \
    --ServiceMetaData.ServiceChargeType POSTPAID_BY_HOUR \
    --ComputeInfo.ComputeResources.0.BundleType 24G_B*4 \
    --ComputeInfo.ComputeResources.0.Count 1 \
    --ComputeInfo.Replicas 1 \
    --DeploymentConfigs.0.Container.Image.ImageRegistryUrl aicompute.tencentcloudcr.com/aibench/sglang:v0.5.3rc0-hml-mooncake-0.3.6 \
    --DeploymentConfigs.0.Container.Image.ImageRegistryUsername 100038736732 \
    --DeploymentConfigs.0.Container.Image.ImageRegistryPassword eyJhbGciOiJSUzI1NiIsImtpZCI6IkxRSFE6RUlWVDpQN0FZOldVR0c6WVFMNDpWSUhLOjZKM1E6M0UzVDpHSUZSOklKSU46TEQ1UDoyT1pKIn0.eyJvd25lclVpbiI6IjEzMDc3NzQwNjciLCJvcGVyYXRvclVpbiI6IjEwMDAzODczNjczMiIsInRva2VuSWQiOiJkNTE1bGRmam43MnBydnZ1ZDZoZyIsImV4cCI6MjA4MTMxNjI3NywibmJmIjoxNzY1OTU2Mjc3LCJpYXQiOjE3NjU5NTYyNzd9.dMFNi5p2iwavBixwWQaUObCq5ifNCbhx8YxC25EPrGjppLG_uoxWEpRYz53fzD04Wouyg_J3fmFsWE7bkG4vnInv0D9M894nyw3Vt7wC3whKa_2R73xXAD54JHFPCtxrJP5BQJN3uoAG_5eb7b-eWc0DqzsUJdHJbEB70-PtHmIITa4mKM7R3SmrI8Ze4KIutuYlpGipShdmcrO0r4gpvITnRvAI9CwPe5t1bdjQKeBp1cMxvXTqXnOV08Hz6l2bx5GnCcLVYrPvYXG9OtIgFsyz5CyCCDw3IHuilgopevklPfYxqBqMSBgwgUA-6AnhdL4qU5MDWp2jHzQ6GFTKxA \
    --DeploymentConfigs.0.Container.Port 30000 \
    --DeploymentConfigs.0.Container.Scripts bash \
    --DeploymentConfigs.0.Container.Envs.0.Name MODEL_DIRECTORY \
    --DeploymentConfigs.0.Container.Envs.0.Value /hai/model \
    --DeploymentConfigs.0.Container.Storages.0.MountPath /hai/model \
    --DeploymentConfigs.0.Container.Storages.0.COSStorage.URI cos://hai-model-bj-1319662662/DeepSeek-R1-Distill-Qwen-7B \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.HttpGet.Path /health \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.HttpGet.Port 30000 \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.InitialDelaySeconds 300 \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.PeriodSeconds 35 \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.TimeoutSeconds 35 \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.SuccessThreshold 1 \
    --DeploymentConfigs.0.Container.Probe.LivenessProbe.FailureThreshold 240 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.HttpGet.Path /health \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.HttpGet.Port 30000 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.InitialDelaySeconds 600 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.PeriodSeconds 5 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.TimeoutSeconds 10 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.SuccessThreshold 1 \
    --DeploymentConfigs.0.Container.Probe.ReadinessProbe.FailureThreshold 12 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.HttpGet.Path /health \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.HttpGet.Port 30000 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.InitialDelaySeconds 10 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.PeriodSeconds 30 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.TimeoutSeconds 30 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.SuccessThreshold 1 \
    --DeploymentConfigs.0.Container.Probe.StartupProbe.FailureThreshold 400 \
    --DeploymentConfigs.0.ContainerCount 1 \
    --NetworkSetting.PublicEndpointEnable True
```

Output: 
```
{
    "Response": {
        "ServiceId": "svc-4lgsk0ja",
        "RequestId": "92137f9d-7e5e-4312-9c97-bb1cf7971854"
    }
}
```

