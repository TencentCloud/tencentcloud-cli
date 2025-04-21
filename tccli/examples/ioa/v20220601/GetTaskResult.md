**Example 1: 获取导入文件异步任务执行结果**

获取导入文件异步任务执行结果

Input: 

```
tccli ioa GetTaskResult --cli-unfold-argument  \
    --TaskID abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskID": "abc",
            "TaskSTate": "abc",
            "ErrorMsg": "abc"
        },
        "RequestId": "abc"
    }
}
```

