**Example 1: 修改推理服务信息**

修改推理服务描述及资源信息。

Input: 

```
tccli teo ModifyInferenceService --cli-unfold-argument  \
    --ZoneId zone-3eox****5tad \
    --ServiceId inf-lwdnt***rgss \
    --ListenPort 8080 \
    --RequestPaths /v1/predictions \
    --Containers.0.ImageType TCR \
    --Containers.0.TcrRepositoryConfig.TCRType Personal \
    --Containers.0.TcrRepositoryConfig.Image ccr.ccs.tencentyun.com/namespace/image:v1.0.0 \
    --Containers.0.TcrRepositoryConfig.RegionName ap-guangzhou \
    --Containers.0.StartupCommand python app.py \
    --Containers.0.EnvironmentVariables.0.Key MODEL_PATH \
    --Containers.0.EnvironmentVariables.0.Value /models/v1 \
    --ResourceConfig.ScalingMode Manual \
    --ResourceConfig.ManualInstanceConfig.FixedInstanceCount 1 \
    --ResourceConfig.Concurrency 10 \
    --Description Image inference based on ResNet50 model
```

Output: 
```
{
    "Response": {
        "RequestId": "c6e1ea80-881c-46f7-bc9b-c55c7a1befa8"
    }
}
```

