**Example 1: 分页获取任务脚本**

分页获取任务脚本

Input: 

```
tccli wedata GetPaginationTaskScript --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId abc \
    --PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ProjectId": "abc",
                "TaskId": "abc",
                "PageSize": 0,
                "PageNum": 0,
                "PageTotal": 0,
                "Base64ScriptContent": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

