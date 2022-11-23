**Example 1: 查询模型加速引擎版本列表**



Input: 

```
tccli tione DescribeModelAccEngineVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ModelAccEngineVersions": [
            {
                "EngineVersions": [
                    {
                        "Image": "tione.tencentcloudcr.com/qcloud-ti-platform/ti-cloud-infer-pytorch-gpu:py38-torch1.9.0-cu111-1.0.1",
                        "Version": "v1.0"
                    }
                ],
                "ModelFormat": "TORCH_SCRIPT"
            }
        ],
        "RequestId": "ced11c16-fd5a-4f12-8a0b-17c7f0b14659"
    }
}
```

