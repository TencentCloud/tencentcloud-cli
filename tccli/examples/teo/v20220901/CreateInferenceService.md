**Example 1: 创建推理服务**

创建推理服务。

Input: 

```
tccli teo CreateInferenceService --cli-unfold-argument  \
    --ZoneId zone-3*********hx \
    --Name ***-test-060202 \
    --ListenPort 5000 \
    --Containers.0.ImageType TCR \
    --Containers.0.TcrRepositoryConfig.TCRType Personal \
    --Containers.0.TcrRepositoryConfig.Image ccr.ccs.tencentyun.com/*******/de****est:cc-1.0 \
    --Containers.0.TcrRepositoryConfig.RegionName ap-guangzhou \
    --ResourceConfig.ScalingMode Manual \
    --ResourceConfig.HardwareSpec spec-******1g \
    --ResourceConfig.ManualInstanceConfig.FixedInstanceCount 1 \
    --ResourceConfig.Concurrency 1 \
    --RequestPaths /predictions
```

Output: 
```
{
    "Response": {
        "ServiceId": "inf-xm*******fvt",
        "RequestId": "815eada4-858c-45a7-8373-eadf09e6ab2e"
    }
}
```

