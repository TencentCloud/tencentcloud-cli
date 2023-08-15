**Example 1: 失败示例**

AI任务不存在

Input: 

```
tccli iss UpdateAITaskStatus --cli-unfold-argument  \
    --TaskId at**********************1 \
    --Status on
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.AITaskNotExisted",
            "Message": "AI任务不存在"
        },
        "RequestId": "52909083-c1eb-4103-a49e-f6d7d078b70b"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss UpdateAITaskStatus --cli-unfold-argument  \
    --TaskId at**********************8 \
    --Status on
```

Output: 
```
{
    "Response": {
        "RequestId": "38686c50-9777-4588-b7b9-c79a216cfe89"
    }
}
```

