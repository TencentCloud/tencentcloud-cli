**Example 1: 设置任务输入参数**

设置任务输入参数

Input: 

```
tccli wedata CreateTaskInParamDs --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId 123123 \
    --ParamKey abc \
    --ParamDesc abc \
    --FromTaskId abc \
    --FromParamKey abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

