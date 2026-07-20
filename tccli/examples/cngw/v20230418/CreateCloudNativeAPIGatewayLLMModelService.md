**Example 1: 创建模型服务**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-aeb0be15 \
    --Name tione-3 \
    --ServiceType LLMService \
    --ModelProvider tione \
    --ModelProtocol OpenAI-Tione \
    --ModelSelector PassThrough \
    --SecretKeyIds secret-f4e97d19d1e876 \
    --EnableModelFallback False \
    --EnableModelParamCheck False \
    --UpstreamURL https://ms-84cnfq44-100011913960.gw.ap-guangzhou.ti.tencentcs.com/ms-84cnfq44 \
    --ExternalInstanceId ins-test2
```

Output: 
```
{
    "Response": {
        "ModelServiceId": "0226dd421d434f68ab414116737c18fc",
        "Result": true,
        "RequestId": "8a41f3c4-7acb-45b0-b9ad-eab01b24643e"
    }
}
```

