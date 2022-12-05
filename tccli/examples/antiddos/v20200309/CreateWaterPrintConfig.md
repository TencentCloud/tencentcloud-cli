**Example 1: 添加DDoS防护的水印防护配置**



Input: 

```
tccli antiddos CreateWaterPrintConfig --cli-unfold-argument  \
    --InstanceId bgp-111111aj \
    --WaterPrintConfig.Keys.0.KeyVersion fbf1 \
    --WaterPrintConfig.Keys.0.KeyContent 82e352b956e8d512-fbf1-82e352b956e8d512eeb95315d5772e86fac99256 \
    --WaterPrintConfig.Keys.0.KeyId 000005hj \
    --WaterPrintConfig.Keys.0.KeyOpenStatus 0 \
    --WaterPrintConfig.Keys.0.CreateTime 2020-09-22 00:00:00 \
    --WaterPrintConfig.Verify checkall \
    --WaterPrintConfig.Listeners.0.ForwardProtocol TCP \
    --WaterPrintConfig.Listeners.0.FrontendPort 88 \
    --WaterPrintConfig.Listeners.0.FrontendPortEnd 88 \
    --WaterPrintConfig.OpenStatus 0 \
    --WaterPrintConfig.Offset 5
```

Output: 
```
{
    "Response": {
        "RequestId": "512b8c34-3df9-448a-ae90-c28643d351bf"
    }
}
```

