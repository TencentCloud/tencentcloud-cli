**Example 1: 检索上下文日志**

检索上下文日志

Input: 

```
tccli cls DescribeLogContext --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --BTime 2021-04-25 14:25:00.000 \
    --PkgId 528C1318606EFEB8-1A7 \
    --PkgLogId 65536 \
    --PrevLogs 10 \
    --NextLogs 10
```

Output: 
```
{
    "Response": {
        "LogContextInfos": [
            {
                "BTime": 1706685527008,
                "Content": "{\"create_time\":\"2022-06-07 17:17:10\",\"Caller\":\"cache/topic.go:92\",\"Time\":\"2024-01-31 15:18:46\",\"Level\":\"INFO\"}",
                "Filename": "/var/log/cls_cgi.log",
                "HighLights": [
                    {
                        "Key": "user_topic_id",
                        "Values": [
                            "<cls_highlight>74ee1b12-9b3d-4a2b-80dd-8322c74126fb</cls_highlight>"
                        ]
                    }
                ],
                "HostName": "eks",
                "IndexStatus": "",
                "PkgId": "5BD4618A65B32B70-117",
                "PkgLogId": 30736474,
                "RawLog": "",
                "Source": "9.148.222.202"
            },
            {
                "BTime": 1706685528008,
                "Content": "{\"create_time\":\"2022-06-07 17:17:10\",\"Caller\":\"cache/topic.go:92\",\"Time\":\"2024-01-31 15:18:46\",\"Level\":\"INFO\"}",
                "Filename": "/var/log/cls_cgi.log",
                "HighLights": [
                    {
                        "Key": "user_topic_id",
                        "Values": [
                            "<cls_highlight>74ee1b12-9b3d-4a2b-80dd-8322c74126fb</cls_highlight>"
                        ]
                    }
                ],
                "HostName": "eks",
                "IndexStatus": "",
                "PkgId": "5BD4618A65B32B70-118",
                "PkgLogId": 42008582,
                "RawLog": "",
                "Source": "9.148.222.202"
            }
        ],
        "NextOver": true,
        "PrevOver": true,
        "RequestId": "0d6109ac-e925-4670-9ccc-dc2bd4024a32"
    }
}
```

