**Example 1: 自定义部署示例**



Input: 

```
tccli hai DeployInferService --cli-unfold-argument  \
    --ServiceMetaData.ServiceName infer \
    --ServiceMetaData.ServiceChargeType PREPAID_BY_MONTH \
    --ComputeInfo.ComputeResources.0.BundleType 96G_A*1 \
    --ComputeInfo.ComputeResources.0.Count 1 \
    --ComputeInfo.Replicas 1 \
    --DeploymentConfigs.0.Container.Image.ImageRegistryUrl haihub.cn \
    --ServiceChargePrepaid.Period 1 \
    --ServiceChargePrepaid.TimeUnit MONTH \
    --ServiceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "ServiceId": "svc-6cjxl264",
        "RequestId": "1a6b1ac1-97b9-4b72-93f8-975fc7441ac8"
    }
}
```

