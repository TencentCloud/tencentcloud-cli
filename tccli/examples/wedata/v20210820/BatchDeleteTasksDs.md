**Example 1: 批量删除任务**

批量删除任务

Input: 

```
tccli wedata BatchDeleteTasksDs --cli-unfold-argument  \
    --TaskIdList abc \
    --DeleteMode True \
    --OperateInform True \
    --ProjectId abc \
    --DeleteScript True
```

Output: 
```
{
    "Response": {
        "Data": {
            "SuccessCount": 0,
            "FailedCount": 0,
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata BatchDeleteTasksDs --cli-unfold-argument  \
    --TaskIdList abc \
    --DeleteMode True \
    --OperateInform True \
    --ProjectId abc \
    --DeleteScript True
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "eb055faf-49d0-452b-9a5b-202343791bcc"
    }
}
```

