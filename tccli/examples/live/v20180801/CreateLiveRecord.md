**Example 1: 创建定时录制任务**

适用于有固定开始时间和结束时间段录制需求的场景， 如培训课堂，商业活动以及节目演出等场景。

Input: 

```
tccli live CreateLiveRecord --cli-unfold-argument  \
    --AppName live \
    --DomainName 5000.live.push.com \
    --StreamName livetest \
    --StartTime 2018-09-11+12%3a04%3a01 \
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

**Example 2: 创建实时录制任务**

适用于直播过程中，遇到精彩画面或因临时需求需要立即开始录制的场景（EndTime 用于指定录制终止时间，录制时长最大支持30分钟）。

Input: 

```
tccli live CreateLiveRecord --cli-unfold-argument  \
    --AppName live \
    --DomainName 5000.live.push.com \
    --StreamName livetest \
    --Highlight 1 \
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

