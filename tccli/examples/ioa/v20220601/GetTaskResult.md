**Example 1: 获取导入文件异步任务执行结果**

获取导入文件异步任务执行结果

Input: 

```
tccli ioa GetTaskResult --cli-unfold-argument  \
    --TaskID 729353f6-4833-47fc-921c-afa1826d5f7f
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskID": "729353f6-4833-47fc-921c-afa1826d5f7f",
            "TaskSTate": "success",
            "ErrorMsg": "成功"
        },
        "RequestId": "z61z353f6-4833-47fc-921c-afa1826d5f7f"
    }
}
```

