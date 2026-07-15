**Example 1: 成功示例**



Input: 

```
tccli tokenhub DescribeModelEndpointList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModelEndpointSet": [
            {
                "ModelId": "hunyuan-role-latest",
                "ModelName": "Hunyuan-role",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "minimax-m2.5",
                "ModelName": "MiniMax-M2.5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "glm-5",
                "ModelName": "GLM-5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2.5",
                "ModelName": "kimi-k2.5",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3.2",
                "ModelName": "Deepseek-v3.2",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "hunyuan-2.0-instruct-20251111",
                "ModelName": "HY 2.0 Instruct",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "hunyuan-2.0-thinking-20251109",
                "ModelName": "HY 2.0 Think",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2-thinking-turbo",
                "ModelName": "kimi-k2-thinking-turbo",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3.1-terminus",
                "ModelName": "Deepseek-v3.1",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "kimi-k2-turbo-preview",
                "ModelName": "kimi-k2-turbo-preview",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-r1-0528",
                "ModelName": "Deepseek-r1-0528",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            },
            {
                "ModelId": "deepseek-v3-0324",
                "ModelName": "Deepseek-v3-0324",
                "PaymentEnabled": false,
                "ServiceType": "TEXT_GENERATION",
                "Status": "INACTIVE"
            }
        ],
        "RequestId": "96f7a35a-31fe-47c1-b481-ff9c95f716ee",
        "TotalCount": 12
    }
}
```

