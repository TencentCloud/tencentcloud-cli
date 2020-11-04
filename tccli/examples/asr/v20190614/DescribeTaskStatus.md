**Example 1: 轮询结果——任务成功**

用户通过轮询方式获取识别结果，任务成功，并返回识别结果。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 2,
            "StatusStr": "success",
            "Result": "[0:0.000,0:2.260,0]  腾讯云语音识别欢迎您。\n",
            "ErrorMsg": ""
        }
    }
}
```

**Example 2: 轮询结果——任务等待**

用户通过轮询方式获取识别结果，任务等待，说明任务还在识别队列中，请用户耐心等候。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 0,
            "StatusStr": "waiting",
            "Result": "",
            "ErrorMsg": ""
        }
    }
}
```

**Example 3: 轮询结果——任务执行中**

用户通过轮询方式获取识别结果，任务执行中，说明任务已经开始识别，请用户耐心等候。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 1,
            "StatusStr": "doing",
            "Result": "",
            "ErrorMsg": ""
        }
    }
}
```

**Example 4: 轮询结果——任务失败**

用户通过轮询方式获取识别结果，任务失败，请用户查看返回的错误码并对照下面的错误码表检查原因。

Input: 

```
tccli asr DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 522931820
```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "TaskId": 522931820,
            "Status": 3,
            "StatusStr": "failed",
            "Result": "",
            "ErrorMsg": "Failed to download audio file!"
        }
    }
}
```

