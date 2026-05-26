**Example 1: 查询单个 LLM 模型服务列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayLLMModelService --cli-unfold-argument  \
    --GatewayId gateway-04b00666 \
    --ModelServiceId 4bc1ed9534b74838a66b9f788cfd2c00
```

Output: 
```
{
    "Response": {
        "RequestId": "2dce5b09-a6d5-4e54-a364-27cb0e859986",
        "Result": {
            "CreateTime": "0001-01-01 00:00:00",
            "Description": "gpt 测试 API-PassThrough",
            "EnableModelParamCheck": true,
            "Id": "4bc1ed9534b74838a66b9f788cfd2c00",
            "ModelParamCheckRule": {
                "AllowModelList": [
                    "gpt-5.1 Pro",
                    "gpt-4o",
                    "gpt-4.1"
                ],
                "ModelValidationFailureStrategy": "Retuen404"
            },
            "ModelProtocol": "OpenAI/v1",
            "ModelProvider": "OpenAI",
            "ModelSelector": "PassThrough",
            "ModifyTime": "0001-01-01 00:00:00",
            "Name": "openai_test_PassThrough",
            "ServiceType": "LLMService"
        }
    }
}
```

