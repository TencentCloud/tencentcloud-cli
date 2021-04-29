**Example 1: 查询事件通知配置**



Input: 

```
tccli vod DescribeEventConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Mode": "PUSH",
        "NotificationUrl": "http://mydemo.com/receiveevent",
        "UploadMediaCompleteEventSwitch": "ON",
        "DeleteMediaCompleteEventSwitch": "OFF",
        "RequestId": "27217d38-95c0-4335-8532-e5154ffb03aa"
    }
}
```

