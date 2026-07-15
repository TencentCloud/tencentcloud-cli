**Example 1: 根据镜像的适用模块过滤**

如下过滤的是开发机依赖的镜像列表

Input: 

```
tccli tione DescribePresetImageList --cli-unfold-argument  \
    --Filters.0.Name ApplicableModule \
    --Filters.0.Values Notebook \
    --Offset 0 \
    --Limit 10 \
    --OrderField ImageName \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "PresetImageList": [
            {
                "ApplicableModuleList": [
                    "Notebook"
                ],
                "ChipTypeList": [
                    "NVIDIA GPU"
                ],
                "ComputeLibVersion": "12.8",
                "CreateTime": "2026-06-15T03:58:16Z",
                "Description": "支持的核心库：Python 3.12.11，CUDA 12.8.93，jupyterlab 4.5.0，torch 2.8.0+cu128，transformers 4.57.1，verl 0.6.1，vllm 0.11.0，ray 2.49.2\n支持的卡型：PNV6，HCCPNV6，H100，H800，L20，L40，A100，A800，A10，V100，T4",
                "ExtraAttributeList": [
                    {
                        "Key": "AllowSaveAllContent",
                        "Type": "",
                        "Value": "true",
                        "Values": []
                    }
                ],
                "Framework": "PYTORCH",
                "FrameworkVersion": "2.8.0",
                "ImageId": "verl0.6.1-vllm0.11.0-torch2.8-py312-cuda12.8-gpu",
                "ImageName": "verl0.6.1-vllm0.11.0-torch2.8-py312-cuda12.8-gpu",
                "ImageRepo": "notebook-conda-gpu",
                "ImageSize": "16638666550",
                "ImageTag": "verl0.6.1-vllm0.11.0-torch2.8-py312-cuda12.8-gpu",
                "ImageType": "TCR",
                "ImageUrl": "tione.tencentcloudcr.com/qcloud-ti-platform/notebook-conda-gpu:verl0.6.1-vllm0.11.0-torch2.8-py312-cuda12.8-gpu",
                "IsLatestStable": true,
                "OS": "Ubuntu 22.04",
                "PythonVersion": "3.12",
                "RuntimeLibList": [
                    {
                        "Name": "verl",
                        "Version": "0.6.1"
                    }
                ],
                "Scenario": "all",
                "SupportDistributedDeploy": false,
                "SupportGpuList": [],
                "UpdateTime": "2026-06-22T13:51:37Z",
                "Version": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "684295f4-579b-4ee0-b8b4-9c0bb264683e"
    }
}
```

**Example 2: 预制镜像列表根据镜像名称过滤**

根据镜像名称搜索

Input: 

```
tccli tione DescribePresetImageList --cli-unfold-argument  \
    --Filters.0.Name ImageName \
    --Filters.0.Values notebook-pytorch
```

Output: 
```
{
    "Response": {
        "PresetImageList": [
            {
                "ApplicableModuleList": [
                    "Notebook"
                ],
                "ChipTypeList": [
                    "CPU only"
                ],
                "ComputeLibVersion": "12.4",
                "CreateTime": "2026-05-19T03:54:42Z",
                "Description": "pytorch 1.12.1通用包（适用模块：notebook、任务式建模、训练算法、推理算法、模型服务，可运行在CPU/GPU芯片上，支持弹性训练任务）",
                "ExtraAttributeList": [],
                "Framework": "PYTORCH",
                "FrameworkVersion": "",
                "ImageId": "notebook-pytorch",
                "ImageName": "notebook-pytorch",
                "ImageRepo": "notebook-pytorch",
                "ImageSize": "7192952533",
                "ImageTag": "py38-cu113-torch1.12.1-v310-250901",
                "ImageUrl": "ccr.ccs.tencentyun.com/ti-platform/notebook-pytorch:py38-cu113-torch1.12.1-v310-250901",
                "IsLatestStable": false,
                "OS": "Ubuntu 22.04",
                "PythonVersion": "3.10",
                "RuntimeLibList": [
                    {
                        "Name": "Triton Server",
                        "Version": "v1.0"
                    }
                ],
                "Scenario": "all",
                "SupportDistributedDeploy": false,
                "SupportGpuList": [],
                "UpdateTime": "2026-05-19T04:03:53Z",
                "Version": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "074859dc-6b97-409d-ba7d-d7dd676f4b22"
    }
}
```

