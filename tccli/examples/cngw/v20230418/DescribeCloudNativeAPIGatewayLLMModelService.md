**Example 1: 查询单个 LLM 模型服务列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-4eb46023 \
    --ModelServiceId d0742b86605340438a8018c658156622
```

Output: 
```
{
    "Response": {
        "Result": {
            "Id": "d0742b86605340438a8018c658156622",
            "Name": "openai_test",
            "CreateTime": "2026-05-19T15:00:00+08:00",
            "ModifyTime": "2026-05-19T15:00:00+08:00",
            "ServiceType": "LLMService",
            "ModelProvider": "openai",
            "ModelProtocol": "OpenAI/V1",
            "UpstreamURL": "",
            "ModelSelector": "Specify",
            "DefaultModel": "gpt-5.1",
            "EnableModelFallback": true,
            "ModelFallbackRule": {
                "FallbackModels": [
                    "gpt-5.2",
                    "gpt-5-mini"
                ]
            },
            "EnableModelParamCheck": false,
            "Description": "OpenAI 模型服务",
            "ConnectTimeout": 10000,
            "WriteTimeout": 60000,
            "ReadTimeout": 60000,
            "Retries": 0,
            "UpstreamUrlMode": "AutoConcat",
            "SNI": ""
        },
        "RequestId": "bb67a5c6-44c2-4ad7-acb4-bffdd4aa68fe"
    }
}
```

