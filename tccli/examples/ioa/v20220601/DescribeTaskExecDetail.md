**Example 1: 获取任务执行详情**

获取任务执行详情

Input: 

```
tccli ioa DescribeTaskExecDetail --cli-unfold-argument  \
    --Condition.PageSize 10 \
    --Condition.PageNum 1 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "An internal error has occurred. Retry your request, but if the problem persists, contact us."
        },
        "RequestId": "e599d550-c039-48bd-8629-320e79fc9e8d"
    }
}
```

