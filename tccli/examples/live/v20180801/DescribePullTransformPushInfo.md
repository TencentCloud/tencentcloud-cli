**Example 1: 请求示例**

查询拉流转推任务的时长信息。

Input: 

```
tccli live DescribePullTransformPushInfo --cli-unfold-argument  \
    --StartTime 2019-02-01T00:00:00+08:00 \
    --EndTime 2019-02-03T00:00:00+08:00 \
    --MainlandOrOversea Mainland
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01T00:00:00+08:00",
                "Duration": 100
            }
        ],
        "TotalDuration": 2000,
        "RequestId": "c8465603-c3a6-44bc-8354-a9b67bf44301"
    }
}
```

