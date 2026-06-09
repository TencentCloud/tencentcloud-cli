**Example 1: 查询模型详情**



Input: 

```
tccli tcr DescribeAIModelVersionDetail --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --NamespaceName ml-models \
    --RepositoryName gpt2-modctl \
    --Reference v1.0
```

Output: 
```
{
    "Response": {
        "Model": {
            "Digest": "sha256:95a32bf97993f391a3135ad26c434e3610c583654d304b0449e626f9f96554e3",
            "Family": "gpt2",
            "FileFormat": "safetensors",
            "Framework": "transformer",
            "IsRecommended": false,
            "ModelName": "gpt2",
            "NamespaceName": "ml-models",
            "ParamSize": "124m",
            "Precision": "fp32",
            "PushTime": "2026-03-24T05:06:55.444Z",
            "Size": 550966200,
            "Version": "v1.0"
        },
        "RequestId": "598203d2-41fe-46d6-a974-5d89f89acc8c"
    }
}
```

