**Example 1: 创建推理服务**

创建推理服务。

Input: 

```
tccli teo CreateInferenceService --cli-unfold-argument  \
    --ZoneId zone-************ \
    --Name ***affinity******* \
    --ListenPort 5000 \
    --Containers.0.ImageType TCR \
    --Containers.0.TcrRepositoryConfig.TCRType Personal \
    --Containers.0.TcrRepositoryConfig.Image ccr.ccs.tencentyun.com/*********************************************** \
    --Containers.0.TcrRepositoryConfig.RegistryId  \
    --Containers.0.TcrRepositoryConfig.RegionName ap-guangzhou \
    --Containers.0.StartupCommand  \
    --ResourceConfig.ScalingMode Manual \
    --ResourceConfig.HardwareSpec spec-******** \
    --ResourceConfig.ManualInstanceConfig.FixedInstanceCount 1 \
    --ResourceConfig.Concurrency 1 \
    --AffinityConfig.Switch On \
    --AffinityConfig.AffinityMode SessionId \
    --AffinityConfig.SessionIdAffinityConfig.Source Header \
    --AffinityConfig.SessionIdAffinityConfig.HeaderName EO-Infer-Session-Id \
    --RequestPaths /predictions \
    --Description 
```

Output: 
```
{
    "Response": {
        "ServiceId": "inf-************",
        "RequestId": "ec2ab94a-7f28-49a6-a59d-2525e4dc5e49"
    }
}
```

