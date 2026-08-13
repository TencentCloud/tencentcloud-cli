**Example 1: 修改推理服务信息**

修改推理服务描述及资源信息。

Input: 

```
tccli teo ModifyInferenceService --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ServiceId inf-************ \
    --ListenPort 5000 \
    --Containers.0.ImageType TCR \
    --Containers.0.TcrRepositoryConfig.TCRType Personal \
    --Containers.0.TcrRepositoryConfig.Image ccr.ccs.tencentyun.com/*********************************************** \
    --Containers.0.TcrRepositoryConfig.RegistryId  \
    --Containers.0.TcrRepositoryConfig.RegionName ap-guangzhou \
    --Containers.0.StartupCommand  \
    --ResourceConfig.ScalingMode Manual \
    --ResourceConfig.ManualInstanceConfig.FixedInstanceCount 1 \
    --ResourceConfig.Concurrency 1 \
    --AffinityConfig.Switch Off \
    --AffinityConfig.AffinityMode SessionId \
    --AffinityConfig.SessionIdAffinityConfig.Source Header \
    --AffinityConfig.SessionIdAffinityConfig.HeaderName EO-Infer-Session-Id
```

Output: 
```
{
    "Response": {
        "RequestId": "e7f97328-5fbf-43f5-be1e-7efc8404880d"
    }
}
```

