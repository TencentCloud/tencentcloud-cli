**Example 1: 更新函数配置**



Input: 

```
tccli tcb UpdateFunctionConfiguration --cli-unfold-argument  \
    --EnvId playground-2g2mc217d35d5e5e \
    --FunctionName wxpayFunctions \
    --Description 微信支付云模板内置云函数 \
    --MemorySize 512 \
    --Timeout 20 \
    --Environment.Variables.0.Key  \
    --Environment.Variables.0.Value  \
    --VpcConfig.VpcId  \
    --VpcConfig.SubnetId  \
    --PublicNetConfig.PublicNetStatus ENABLE \
    --PublicNetConfig.EipConfig.EipStatus DISABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "uuid"
    }
}
```

