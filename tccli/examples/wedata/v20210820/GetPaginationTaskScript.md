**Example 1: 分页获取任务脚本**

分页获取任务脚本

Input: 

```
tccli wedata GetPaginationTaskScript --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --TaskId 20250808113834792
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Base64ScriptContent": "IyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IGphc29uemN3YW5nCiMjY3JlYXRlIHRpbWU6IDIwMjUtMDgtMDggMTE6Mzg6MzAKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKcHJpbnQoIjEiKQ==",
                "PageNum": 1,
                "PageSize": 4096,
                "PageTotal": 1,
                "ProjectId": "1470547050521227264",
                "TaskId": "20250808113834792"
            }
        ],
        "RequestId": "1925b36c-ef69-4aad-be44-974eb9adc05e"
    }
}
```

