**Example 1: 示例**



Input: 

```
tccli dlc GetInferenceModel --cli-unfold-argument  \
    --ModelUid m-qwen3-5-4b-6a223aba-951c
```

Output: 
```
{
    "Response": {
        "AppId": 0,
        "BuiltIn": true,
        "CreateTime": 1780628154611,
        "Description": "Qwen3.5-4B 是阿里云通义千问团队推出的小尺寸稠密语言模型，采用原生多模态训练与最新模型架构，支持 256K 上下文长度，适用于端侧及边缘设备的高性能轻量级应用场景。",
        "HasCustomStorage": false,
        "HasStorage": true,
        "LatestVersion": "v1",
        "ModelId": "20",
        "ModelType": "LLM",
        "ModelUid": "m-qwen3-5-4b-6a223aba-951c",
        "Name": "Qwen3.5-4B",
        "ParameterSize": "4B",
        "Provider": "Qwen",
        "ServiceCount": 5,
        "StorageType": "COS",
        "SubAccountUin": "system",
        "SupportedEngines": [
            "vllm"
        ],
        "Tags": [
            "对话"
        ],
        "Tasks": [
            "Text Generation"
        ],
        "Uin": "system",
        "UpdateTime": 1780628154611,
        "VersionCount": 1,
        "RequestId": "de055bc8-f7bc-4c71-bbae-d09238c51286"
    }
}
```

