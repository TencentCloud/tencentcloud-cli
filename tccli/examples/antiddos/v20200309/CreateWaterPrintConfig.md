**Example 1: 添加DDoS防护的水印防护配置**



Input: 

```
tccli antiddos CreateWaterPrintConfig --cli-unfold-argument  \
    --InstanceId xx \
    --WaterPrintConfig.Keys.0.KeyVersion xx \
    --WaterPrintConfig.Keys.0.KeyContent xx \
    --WaterPrintConfig.Keys.0.KeyId xx \
    --WaterPrintConfig.Keys.0.KeyOpenStatus 0 \
    --WaterPrintConfig.Keys.0.CreateTime 2020-09-22 00:00:00 \
    --WaterPrintConfig.Verify xx \
    --WaterPrintConfig.Listeners.0.ForwardProtocol xx \
    --WaterPrintConfig.Listeners.0.FrontendPort 0 \
    --WaterPrintConfig.Listeners.0.FrontendPortEnd 0 \
    --WaterPrintConfig.OpenStatus 0 \
    --WaterPrintConfig.Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "512b8c34-3df9-448a-ae90-c28643d351bf"
    }
}
```

