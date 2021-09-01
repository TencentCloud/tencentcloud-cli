**Example 1: 获取项目列表**



Input: 

```
tccli cme DescribeProjects --cli-unfold-argument  \
    --Platform test \
    --ProjectIds 1111
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectInfoSet": [
            {
                "ProjectId": "1111",
                "Name": "test",
                "AspectRatio": "16:9",
                "Category": "VIDEO_EDIT",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "user_1233"
                },
                "StreamConnectProjectInfo": null,
                "UpdateTime": "2020-11-13T06:41:34.808Z",
                "CreateTime": "2020-11-13T06:41:34.808Z",
                "CoverUrl": ""
            }
        ],
        "RequestId": "requestId"
    }
}
```

**Example 2: 获取云转推项目信息**



Input: 

```
tccli cme DescribeProjects --cli-unfold-argument  \
    --Platform test \
    --ProjectIds 1111 \
    --CategorySet STREAM_CONNECT
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectInfoSet": [
            {
                "ProjectId": "1111",
                "Name": "test",
                "AspectRatio": "16:9",
                "Category": "STREAM_CONNECT",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "user_1233"
                },
                "UpdateTime": "2020-11-13T06:41:34.808Z",
                "CreateTime": "2020-11-13T06:41:34.808Z",
                "CoverUrl": "",
                "StreamConnectProjectInfo": {
                    "Status": "Working",
                    "CurrentInputEndpoint": "Main",
                    "CurrentStartTime": "2020-11-13T06:41:34.808Z",
                    "CurrentStopTime": "2020-11-13T08:41:34.808Z",
                    "LastStopTime": "2020-11-12T07:41:34.808Z",
                    "MainInput": {
                        "InputType": "LivePull",
                        "LivePullInputInfo": {
                            "InputUrl": "rtmp://liveplay.video-studio.myqcloud.com/output/1250000001-600e8e7fb1cc1c0001293759?txSecret=d5f0d5e9eadda723d7fbf6822313b1c0&txTime=6017C8FF"
                        }
                    },
                    "OutputSet": [
                        {
                            "PushSwitch": "On",
                            "StreamConnectOutput": {
                                "Id": "124522",
                                "PushUrl": "rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08",
                                "Name": "test"
                            }
                        }
                    ]
                }
            }
        ],
        "RequestId": "60599df66a6b440001518159"
    }
}
```

