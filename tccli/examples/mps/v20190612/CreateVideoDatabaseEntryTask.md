**Example 1: Url视频入库**

使用视频url发起视频入库任务

Input: 

```
tccli mps CreateVideoDatabaseEntryTask --cli-unfold-argument  \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url http://qq.com/test.mp4 \
    --TaskNotifyConfig.NotifyType URL \
    --TaskNotifyConfig.NotifyUrl http://qq.com/callback
```

Output: 
```
{
    "Response": {
        "TaskId": "251xxx279-VideoDBEntryTask-60e4ae3b23ff4fd3936eb6b7e8af25ec",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: COS视频入库**

使用视频COS地址发起视频入库任务

Input: 

```
tccli mps CreateVideoDatabaseEntryTask --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket test-bucket \
    --InputInfo.CosInputInfo.Region ap-nanjing \
    --InputInfo.CosInputInfo.Object /movie/test.mp4 \
    --TaskNotifyConfig.NotifyType URL \
    --TaskNotifyConfig.NotifyUrl http://qq.com/callback
```

Output: 
```
{
    "Response": {
        "TaskId": "251xxx279-VideoDBEntryTask-60e4ae3b23ff4fd3936eb6b7e8af25ec",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

