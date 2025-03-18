**Example 1: 示例**



Input: 

```
tccli tione DescribePlatformImages --cli-unfold-argument  \
    --Offset 0 \
    --Limit 200 \
    --Filters.0.Name ImageRange \
    --Filters.0.Values Train
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PlatformImageInfos": [
            {
                "Framework": "PYTORCH",
                "ImageType": "TCR",
                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/llm-train:24.03-gpu-py310-cu124-tilearn-llm-v1.8.0",
                "RegistryRegion": "",
                "RegistryId": "",
                "ImageName": "tilearn-llm0.9-torch2.3-py3.10-cuda12.4-gpu",
                "ImageId": "35551e3c-b0e3-40dc-8e91-cc10a5613cd3",
                "FrameworkVersion": "2.3",
                "SupportGpuList": [
                    "A10",
                    "V100",
                    "T4"
                ],
                "Description": "支持的核心库：Python 3.10，CUDA 12.4，jupyterlab 2.3.2，torch 2.3.0a0+40ec155e58.nv24.3，transformers 4.39.3，deepspeed 0.13.4，tilearn-llm 0.9.9，tilearn.ops 0.2.2.175，angel-vllm 0.4.2\n支持的卡型：A10，V100，T4",
                "ImageRange": [
                    "Notebook",
                    "Train"
                ],
                "ExtraAttributes": [
                    {
                        "Type": "",
                        "Key": "AllowSaveAllContent",
                        "Value": "true",
                        "Values": []
                    },
                    {
                        "Type": "",
                        "Key": "SupportDataPipeline",
                        "Value": "false",
                        "Values": []
                    },
                    {
                        "Type": "List",
                        "Key": "TrainingModes",
                        "Value": "",
                        "Values": [
                            "DDP"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "8a3942be-0e3c-4efd-bf03-422e0410afa9"
    }
}
```

