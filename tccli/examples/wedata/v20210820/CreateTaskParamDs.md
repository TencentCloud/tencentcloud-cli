**Example 1: 创建任务引用参数**

创建任务引用参数

Input: 

```
tccli wedata CreateTaskParamDs --cli-unfold-argument  \
    --ProjectId 1231231 \
    --Request.0.TaskId abc \
    --Request.0.MapParamList.0.Key abc \
    --Request.0.MapParamList.0.Value abc
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

