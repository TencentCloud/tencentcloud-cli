**Example 1: API调用**



Input: 

```
tccli tts DescribeTtsTaskStatus --cli-unfold-argument  \
    --TaskId ed461a019355c5cd1ce31ab4dfb8cb12
```

Output: 
```
{
    "Response": {
        "RequestId": "ed461a0-19355c5-cd1ce31-ab4dfb8cb12",
        "Data": {
            "TaskId": "ed461a019355c5cd1ce31ab4dfb8cb12",
            "Status": 0,
            "StatusStr": "waiting in queue",
            "ResultUrl": "",
            "ErrorMsg": ""
        }
    }
}
```

