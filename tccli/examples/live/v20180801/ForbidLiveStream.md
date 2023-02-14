**Example 1: 请求示例**

对直播推流进行封禁。

Input: 

```
tccli live ForbidLiveStream --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName stream1 \
    --ResumeTime 2018-11-24T12:00:00Z
```

Output: 
```
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

