**Example 1: CreateTask**



Input: 

```
tccli cpp CreateTask --cli-unfold-argument  \
    --TaskName abc \
    --EndTime abc \
    --StartTime abc \
    --MonitorPlatform abc \
    --WhiteList.0.Type abc \
    --WhiteList.0.Name abc \
    --WhiteList.0.Platform abc \
    --MediaType 0
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

