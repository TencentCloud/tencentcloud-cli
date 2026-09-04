**Example 1: 获取模型任务类型选项**



Input: 

```
tccli dlc DescribeModelTaskOptions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskOptions": [
            {
                "ModelType": "LLM",
                "Tasks": [
                    "Text Generation"
                ]
            }
        ],
        "RequestId": "8e95acf9-8a9e-4498-8023-c3a2e18ae933"
    }
}
```

