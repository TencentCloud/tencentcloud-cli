**Example 1: 停止多个任务的调试**

停止多个任务的调试

Input: 

```
tccli wedata KillTasksTestRun --cli-unfold-argument  \
    --Id abc \
    --TaskIds abc
```

Output: 
```
{
    "Response": {
        "Id": "abc",
        "Results": [
            {
                "TaskId": "abc",
                "Status": "abc",
                "Message": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

