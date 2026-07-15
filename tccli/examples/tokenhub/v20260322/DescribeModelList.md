**Example 1: DescribeModelList**

查询模型列表，支持按模型 ID、模型名称、模型能力等条件筛选，支持分页和排序。

Input: 

```
tccli tokenhub DescribeModelList --cli-unfold-argument  \
    --ModelIds deepseek-v3.2
```

Output: 
```
{
    "Response": {
        "ModelSet": [
            {
                "Brand": "DeepSeek",
                "Description": "DeepSeek-V3.2 为685B 参数 MoE 模型，其引入的稀疏注意力架构使长文本处理更高效，并在推理评测中达到GPT-5水平。",
                "DisplayName": "Deepseek-v3.2",
                "FreeTrialInfo": {
                    "CapacitySize": 500000,
                    "RecommendWeight": 7,
                    "Unit": "token"
                },
                "ModelAccessInfo": {
                    "ModelSiteRegions": [
                        {
                            "Regions": [
                                "ap-singapore"
                            ],
                            "Site": "domestic"
                        },
                        {
                            "Regions": [
                                "ap-singapore"
                            ],
                            "Site": "international"
                        }
                    ]
                },
                "ModelChargingInfo": [
                    {
                        "Name": "",
                        "Type": "Uniform"
                    }
                ],
                "ModelId": "deepseek-v3.2",
                "ModelImage": {
                    "Url": "https://qcloudimg.tencent-cloud.cn/raw/eb73bf9964b1e5a67cd798270fc55ce4.png"
                },
                "ModelName": "Deepseek-v3.2",
                "ModelSpec": {
                    "ContextLength": "128k",
                    "MaxInputToken": "96k",
                    "MaxOutputToken": "32k",
                    "QPM": "15000",
                    "TPM": "30w"
                },
                "ModelType": "Text",
                "Provider": "三方",
                "RecommendWeight": 21,
                "ReleaseAt": "2025-12-02T00:00:00+08:00",
                "Status": "online",
                "Tags": [
                    "深度思考",
                    "文本生成"
                ]
            }
        ],
        "RequestId": "319fc5ca-3fed-44a4-9a71-36bd0f6899fc",
        "TotalCount": 1
    }
}
```

