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
            "TaskId": "ce68122c-0ca8-4fa6-99b1-90a2867",
            "Status": 2,
            "StatusStr": "waiting in queue",
            "VoiceType": 200000000,
            "FastVoiceType": "WCHN-353xxxx0f3eace0c1",
            "ErrorMsg": ""
        },
        "RequestId": "63f43c3d6e30af6bd63735b0"
    }
}
```

