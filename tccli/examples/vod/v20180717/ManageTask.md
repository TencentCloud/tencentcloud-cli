**Example 1: 终止正在执行中的直播流处理任务示例**

正在执行中的直播流处理任务，调用接口终止。

Input: 

```
tccli vod ManageTask --cli-unfold-argument  \
    --TaskId 251000333-procedure-c27bdf65ea06646171e714f25f5aac6 \
    --OperationType Abort
```

Output: 
```
{
    "Response": {
        "RequestId": "510f4d68-09c9-44a3-ab55-192ff22297c9"
    }
}
```

