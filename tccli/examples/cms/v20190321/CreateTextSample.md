**Example 1: 新增文本样本**

将“测试”关键词加入自定义词库，并设置该词类型为正常

Input: 

```
tccli cms CreateTextSample --cli-unfold-argument  \
    --Label 2 \
    --EvilType 100 \
    --Contents 测试
```

Output: 
```
{
    "Response": {
        "RequestId": "c1935701-668a-4e0f-9f25-7e88a5f3f7af",
        "Progress": 2,
        "ErrMsg": "3:-1009,4:-1009,"
    },
    "retcode": 0,
    "retmsg": "success"
}
```

