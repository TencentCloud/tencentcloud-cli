**Example 1: 查询应用**

查询应用

Input: 

```
tccli hai DescribeApplications --cli-unfold-argument  \
    --ApplicationIds app-7j7f9jhn \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "ApplicationSet": [
            {
                "ApplicationId": "app-7j7f9jhn",
                "ApplicationName": "混元-DiT WebUI",
                "ApplicationSize": 120,
                "ApplicationState": "ONLINE",
                "ApplicationType": "PUBLIC_APPLICATION",
                "ConfigEnvironment": "Ubuntu20.04, Python 3.8.12, CUDA 11.7, cuDNN 8, HunYuanDiT, JupyterLab, Gradio",
                "CreateTime": "2024-07-11 16:36:08",
                "Description": "混元-DiT是腾讯自研的高性能细粒度中文理解多分辨率扩散Transformer模型。提供双语生成能力，中国元素理解具有优势。",
                "MinSystemDiskSize": 150
            }
        ],
        "RequestId": "c344dc00-13a2-4d80-ae95-6e2d9fd0105d",
        "TotalCount": 1
    }
}
```

