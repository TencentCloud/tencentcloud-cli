**Example 1: 失败示例**

AI任务不存在

Input: 

```
tccli iss DeleteAITask --cli-unfold-argument  \
    --TaskId at**********************1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.AITaskNotExisted",
            "Message": "AI任务不存在"
        },
        "RequestId": "3eb1421c-36cf-420d-8f4b-cce8f68168af"
    }
}
```

**Example 2: 成功示例**

无

Input: 

```
tccli iss DeleteAITask --cli-unfold-argument  \
    --TaskId at**********************8
```

Output: 
```
{
    "Response": {
        "RequestId": "e7c7cfd4-0866-468d-a165-c9ec5837fb28"
    }
}
```

