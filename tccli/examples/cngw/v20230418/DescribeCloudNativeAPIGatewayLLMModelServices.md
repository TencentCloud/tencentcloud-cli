**Example 1: 查询模型服务**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewayLLMModelServices --cli-unfold-argument  \
    --GatewayId gateway-0703606b \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "DataList": [
                {
                    "ConnectTimeout": 10000,
                    "CreateTime": "2026-05-18 09:02:49",
                    "Description": "",
                    "EnableModelParamCheck": false,
                    "Id": "d0742b86605340438a8018c658156622",
                    "ModelProtocol": "OpenAI-Custom",
                    "ModelProvider": "custom",
                    "ModelSelector": "PassThrough",
                    "ModifyTime": "2026-05-18 09:02:49",
                    "Name": "custom",
                    "ReadTimeout": 60000,
                    "Retries": 0,
                    "SNI": "generativelanguage.googleapis.com",
                    "ServiceType": "LLMService",
                    "UpstreamURL": "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent",
                    "UpstreamUrlMode": "FixedPath",
                    "WriteTimeout": 60000
                }
            ],
            "TotalCount": 2
        },
        "RequestId": "faeffc01-bda7-4fec-8407-7d8198b0bda9"
    }
}
```

