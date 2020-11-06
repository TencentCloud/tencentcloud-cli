**Example 1: 请求示例**

当某些原因暂停主播继续推流时，可调用此接口

Input: 

```
tccli live DropLiveStream --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com \
    --AppName live \
    --StreamName stream1
```

Output: 
```
{
    "Response": {
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

