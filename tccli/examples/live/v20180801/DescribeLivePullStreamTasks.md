**Example 1: 请求示例**

查询直播拉流任务。

Input: 

```
tccli live DescribeLivePullStreamTasks --cli-unfold-argument  \
    --TaskId 123
```

Output: 
```
{
    "Response": {
        "TaskInfos": [
            {
                "AppName": "live",
                "Region": "ap-beijing",
                "CallbackInfo": "",
                "CallbackEvents": [
                    "TaskStart",
                    "TaskExit"
                ],
                "CallbackUrl": "",
                "CreateBy": "yourname",
                "DomainName": "yourdomain.com",
                "EndTime": "2020-04-25T00:30:00Z",
                "ErrorInfo": "",
                "PushArgs": "txsecret=7cbb8f382a21e8d2f6cd8098100d3b8e&txtime=5ea0450d",
                "SourceType": "PullLivePushLive",
                "SourceUrls": [
                    "http://yourdomain/live/test.flv"
                ],
                "StartTime": "2020-04-20T00:30:00Z",
                "Status": "enable",
                "StreamName": "teststream",
                "Comment": "abc",
                "TaskId": "10054",
                "UpdateBy": "",
                "UpdateTime": "2020-04-23T05:07:43Z",
                "CreateTime": "2020-04-20T05:07:43Z",
                "VodLoopTimes": -1,
                "VodRefreshType": "ImmediateNewSource",
                "VodLocalMode": 0,
                "BackupSourceType": "",
                "BackupSourceUrl": "",
                "WatermarkList": [],
                "RecentPullInfo": {
                    "FileUrl": "http://yourdomain/live/test.flv",
                    "OffsetTime": 95,
                    "LoopedTimes": 0,
                    "ReportTime": "2020-04-23T08:20:39Z"
                }
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "LimitTaskNum": 20,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

