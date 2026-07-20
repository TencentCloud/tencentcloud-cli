**Example 1: 查询推理服务**

按条件筛选查询推理服务。

Input: 

```
tccli teo DescribeInferenceServices --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --Filters.0.Name service-name \
    --Filters.0.Values image-classification \
    --Filters.0.Fuzzy True \
    --Offset 0 \
    --Limit 20 \
    --Order create-time \
    --Direction desc
```

Output: 
```
{
    "Response": {
        "Services": [
            {
                "Containers": [
                    {
                        "EnvironmentVariables": [
                            {
                                "Key": "MODEL_PATH",
                                "Value": "/models/v1"
                            }
                        ],
                        "ImageType": "TCR",
                        "StartupCommand": "python app.py",
                        "TcrRepositoryConfig": {
                            "Image": "ccr.ccs.tencentyun.com/namespace/image:v1.0.0",
                            "RegionName": "ap-guangzhou",
                            "RegistryId": "tcr-ab***ef456",
                            "TCRType": "Enterprise"
                        }
                    }
                ],
                "CreateTime": "2025-12-09T10:00:00Z",
                "Description": "Image inference based on ResNet50 model",
                "InferenceURL": "https://model-zone-***0300.edgeone-ai.com",
                "ListenPort": 8080,
                "Name": "image-classification-service",
                "ResourceConfig": {
                    "AutoScalingConfig": {
                        "MinInstanceCount": 1
                    },
                    "Concurrency": 10,
                    "HardwareSpec": "GPU-T4-8C16G",
                    "ManualInstanceConfig": null,
                    "ScalingMode": "Auto"
                },
                "ServiceId": "inf-9f8***4a3210",
                "Status": "Running",
                "UpdateTime": "2025-12-09T10:30:00Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "36b93c01-c30f-4865-86f7-710067654fea"
    }
}
```

