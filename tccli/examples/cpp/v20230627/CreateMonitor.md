**Example 1: CreateMonitor**



Input: 

```
tccli cpp CreateMonitor --cli-unfold-argument  \
    --TaskName abc \
    --StartTime abc \
    --EndTime abc \
    --MonitorPlatform abc \
    --WhiteList.0.Type abc \
    --WhiteList.0.Name abc \
    --WhiteList.0.Platform abc \
    --WorkList.0.WorksName abc \
    --WorkList.0.PublishTime abc \
    --WorkList.0.MediaType 0 \
    --WorkList.0.WorksAuthor abc \
    --WorkList.0.Url abc \
    --WorkList.0.WorksTag abc \
    --WorkList.0.WorksType abc \
    --WorkList.0.ExtraInfo.Description abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "abc",
            "TaskName": "abc",
            "Works": [
                {
                    "WorkId": "abc",
                    "WorkName": "abc",
                    "Url": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

