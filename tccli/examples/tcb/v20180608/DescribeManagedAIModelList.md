**Example 1: 查询托管模型列表**

查询托管模型列表

Input: 

```
tccli tcb DescribeManagedAIModelList --cli-unfold-argument  \
    --EnvId free-********-7g5aa8xnfd5428b4
```

Output: 
```
{
    "Response": {
        "ManagedAIModelList": [
            {
                "GroupName": "cloudbase",
                "Models": [
                    {
                        "EnableMCP": true,
                        "Model": "deepseek-v3.2",
                        "ModelChargingInfo": [
                            {
                                "InputOutputUnit": "千tokens",
                                "InputPrice": "2",
                                "OutputPrice": "3",
                                "Type": "Uniform"
                            }
                        ],
                        "ModelSpec": {
                            "ContextLength": "128k",
                            "MaxInputToken": "96k",
                            "MaxOutputToken": "32k"
                        }
                    }
                ],
                "Remark": "腾讯云开发"
            }
        ],
        "RequestId": "8a6ee0a7-8708-4eeb-98cd-cd1f22216818"
    }
}
```

