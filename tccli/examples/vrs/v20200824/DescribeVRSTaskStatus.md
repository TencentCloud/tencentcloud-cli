**Example 1: 声音复刻任务结果查询**

声音复刻任务结果查询

Input: 

```
tccli vrs DescribeVRSTaskStatus --cli-unfold-argument  \
    --TaskId ed461a019355c5cd1ce31ab4dfb8cb12
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "ed461a019355c5cd1ce31ab4dfb8cb12",
            "Status": 2,
            "StatusStr": "waiting in queue",
            "VoiceType": 100000,
            "ErrorMsg": ""
        },
        "RequestId": "63f43c3d6e30af6bd63735b0"
    }
}
```

