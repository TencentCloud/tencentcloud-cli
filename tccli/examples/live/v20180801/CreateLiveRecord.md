**Example 1: Creating scheduled recording task**

This example shows you how to create a scheduled recording task, which is suitable for scenarios where the start time and end time of recording are fixed, such as training courses, business events, shows, and performances.

Input: 

```
tccli live CreateLiveRecord --cli-unfold-argument  \
    --AppName live\
    --DomainName 5000.live.push.com\
    --StreamName livetest\
    --StartTime 2018-09-11+12%3a04%3a01\
    --EndTime 2018-09-11+12%3a08%3a01
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": 1234567
    }
}
```

**Example 2: Creating real-time recording task**

This example shows you how to create a real-time recording task, which is suitable for scenarios where recording needs to start immediately to record certain video content or meet temporary needs during live streaming. (`EndTime` is used to specify the recording end time, and the recording can last for up to 30 minutes.)

Input: 

```
tccli live CreateLiveRecord --cli-unfold-argument  \
    --AppName live\
    --DomainName 5000.live.push.com\
    --StreamName livetest\
    --Highlight 1\
    --EndTime 2018-09-11+12%3a08%3a01
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TaskId": 1234567
    }
}
```

