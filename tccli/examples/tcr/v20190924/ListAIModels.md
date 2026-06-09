**Example 1: 获取模型列表**



Input: 

```
tccli tcr ListAIModels --cli-unfold-argument  \
    --RegistryId tcr-kp**letb \
    --Namespace ml-models \
    --Offset 10 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "ModelList": [
            {
                "Digest": "sha256:d745fff298ba0e3bef5e2edcec219c7094e38509a7588476d0d5f6530f22836f",
                "ImageSize": "196237",
                "Kind": "CNAI-Model",
                "LatestVersion": "v1.1.0",
                "ModelName": "t5-small",
                "NamespaceName": "ml-models",
                "UpdateTime": "2026-03-23T13:18:45.513Z"
            }
        ],
        "TotalCount": 15,
        "RequestId": "6ed4aa48-dac4-4ae2-93d2-4e4798180202"
    }
}
```

