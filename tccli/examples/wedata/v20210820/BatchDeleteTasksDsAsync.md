**Example 1: 异步批量删除任务**

异步批量删除任务

Input: 

```
tccli wedata BatchDeleteTasksDsAsync --cli-unfold-argument  \
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
            "JobId": 1
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata BatchDeleteTasksDsAsync --cli-unfold-argument  \
    --TaskIdList 20230425181533351
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "could not execute statement"
        },
        "RequestId": "59fbc826-60d4-4f4b-b1a9-0cbb4dce278a"
    }
}
```

