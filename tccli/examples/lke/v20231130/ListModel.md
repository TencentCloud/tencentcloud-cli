**Example 1: ListModel**

获取模型列表


Input: 

```
tccli lke ListModel --cli-unfold-argument  \
    --AppType knowledge_qa \
    --ModelCategory thought \
    --Pattern agent
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AliasName": "精调知识大模型标准版",
                "MaxTokens": {
                    "Default": 4000,
                    "Max": 8000,
                    "Min": 1
                },
                "ModelDesc": "",
                "ModelName": "cs-normal",
                "PromptWordsLimit": "8K",
                "ResourceStatus": 1,
                "Temperature": {
                    "Default": 0.7,
                    "Max": 1,
                    "Min": 0
                },
                "TopP": {
                    "Default": 0.8,
                    "Max": 1,
                    "Min": 0
                }
            }
        ],
        "RequestId": "53b9fa7e-d4b5-4aec-8229-d56ea3965493"
    }
}
```

