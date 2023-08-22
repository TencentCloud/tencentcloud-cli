**Example 1: API调用**



Input: 

```
tccli tts DescribeTtsTaskStatus --cli-unfold-argument  \
    --TaskId gz-855e1e59-35c2-4e43-b15a-3409c515d62e
```

Output: 
```
{
    "Response": {
        "RequestId": "28e1a307-0381-4e56-863d-42542993bf87",
        "Data": {
            "TaskId": "gz-855e1e59-35c2-4e43-b15a-3409c515d62e",
            "Status": 0,
            "StatusStr": "waiting in queue",
            "ResultUrl": "",
            "Subtitles": [],
            "ErrorMsg": ""
        }
    }
}
```

