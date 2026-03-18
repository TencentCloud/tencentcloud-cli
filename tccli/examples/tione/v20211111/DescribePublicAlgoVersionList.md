**Example 1: 查询公共算法版本列表**



Input: 

```
tccli tione DescribePublicAlgoVersionList --cli-unfold-argument  \
    --Filters.0.Name PublicAlgoGroupId \
    --Filters.0.Values hunyuan_t5_10b_chinese_generation \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 49,
        "PublicAlgoVersions": [],
        "AggregatePublicAlgoVersions": [
            {
                "GroupName": "Hunyuan-Large",
                "PublicAlgoVersions": [
                    {
                        "PublicAlgoSeriesId": "hunyuan_series",
                        "PublicAlgoVersionId": "hunyuan-large-chat-v1",
                        "PublicAlgoGroupId": "Hunyuan-Large-Instruct",
                        "Version": "v1",
                        "Introduction": "#",
                        "PreviewInfo": "",
                        "PresetTrainImageInfo": {
                            "ImageType": "PRE_SET",
                            "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v3.10.2",
                            "RegistryRegion": "",
                            "RegistryId": ""
                        },
                        "PresetTrainCodeInfo": {
                            "StorageType": "CFS",
                            "CosPathInfo": null,
                            "MaterialName": "Code",
                            "MaterialType": "PreSet",
                            "MountPath": "/opt/ml/code"
                        },
                        "PresetModelInfo": {
                            "StorageType": "CFS",
                            "CosPathInfo": {
                                "Bucket": "llm-cfs-sync-bj-1308945662",
                                "Region": "ap-beijing",
                                "Paths": [
                                    "public/models/Hunyuan-A52B-Instruct-128k-20241116"
                                ]
                            },
                            "MaterialName": "Model",
                            "MaterialType": "PreSet",
                            "MountPath": "/opt/ml/pretrain_model"
                        },
                        "IsImported": false,
                        "CreateTime": "2024-09-12T17:11:09+08:00",
                        "UpdateTime": "2025-10-29T20:11:44+08:00",
                        "DefaultResourceSpec": null,
                        "SupportDeploy": true,
                        "DefaultInferenceResourceSpec": null,
                        "PresetTrainDataset": {
                            "StorageType": "CFS",
                            "CosPathInfo": null,
                            "MaterialName": "Data",
                            "MaterialType": "PreSet",
                            "MountPath": "/opt/ml/input/data/train"
                        },
                        "TrainCodeDownloadUrl": "",
                        "TrainParams": [
                            {
                                "Name": "Epoch",
                                "DefaultValue": "2",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "BatchSize",
                                "DefaultValue": "1",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "LearningRate",
                                "DefaultValue": "5e-6",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "Step",
                                "DefaultValue": "500",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "FinetuningType",
                                "DefaultValue": "Lora",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "MaxSequenceLength",
                                "DefaultValue": "2048",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "GradientAccumulationSteps",
                                "DefaultValue": "1",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "GradientCheckPointing",
                                "DefaultValue": "true",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "DeepspeedZeroStage",
                                "DefaultValue": "z3_offload",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            },
                            {
                                "Name": "ResumeFromCheckpoint",
                                "DefaultValue": "true",
                                "Comment": "",
                                "Type": "",
                                "Range": [],
                                "Enum": [],
                                "Required": false,
                                "Value": ""
                            }
                        ],
                        "PresetTrainCodeStartCmd": "cd /opt/ml/code; bash start.sh",
                        "TrainDataDownloadUrl": "https://tione-dev-1256580188.cos.ap-guangzhou.myqcloud.com/ai-market/llm/data/cnn-part-zh.jsonl",
                        "IsPrivateModel": false,
                        "PresetTrainImageInfoList": [
                            {
                                "DeviceType": "GPU",
                                "ImageInfo": {
                                    "ImageType": "PRE_SET",
                                    "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v3.10.2",
                                    "RegistryRegion": "",
                                    "RegistryId": ""
                                }
                            },
                            {
                                "DeviceType": "H20",
                                "ImageInfo": {
                                    "ImageType": "PRE_SET",
                                    "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v1.8.0",
                                    "RegistryRegion": "",
                                    "RegistryId": ""
                                }
                            },
                            {
                                "DeviceType": "HCC-H20",
                                "ImageInfo": {
                                    "ImageType": "PRE_SET",
                                    "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v1.8.0",
                                    "RegistryRegion": "",
                                    "RegistryId": ""
                                }
                            }
                        ],
                        "PresetInferenceImageInfoList": [],
                        "PresetTrainCodeInfoList": [],
                        "PresetModelInfoList": [],
                        "ModelCategory": "LLM"
                    }
                ]
            }
        ],
        "RequestId": "3330975a-a579-4f72-bd25-637434b4cf30"
    }
}
```

