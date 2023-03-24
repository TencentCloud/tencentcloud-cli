**Example 1: 获取项目列表**

 

Input: 

```
tccli cme DescribeProjects --cli-unfold-argument  \
    --Platform test \
    --ProjectIds cmepid_60599df66a6b440001518159
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectInfoSet": [
            {
                "ProjectId": "cmepid_60599df66a6b440001518159",
                "Name": "test",
                "AspectRatio": "16:9",
                "Category": "VIDEO_EDIT",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "user_31345df76a6b44104571916a"
                },
                "StreamConnectProjectInfo": null,
                "MediaCastProjectInfo": null,
                "UpdateTime": "2020-11-13T06:41:34.808Z",
                "CreateTime": "2020-11-13T06:41:34.808Z",
                "CoverUrl": ""
            }
        ],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5c"
    }
}
```

**Example 2: 获取云转推项目信息**

 

Input: 

```
tccli cme DescribeProjects --cli-unfold-argument  \
    --Platform test \
    --CategorySet STREAM_CONNECT \
    --ProjectIds cmepid_60599df66a6b440001518169
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectInfoSet": [
            {
                "ProjectId": "cmepid_60599df66a6b440001518169",
                "Name": "test",
                "AspectRatio": "",
                "Category": "STREAM_CONNECT",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "user_31345df76a6b44104571916a"
                },
                "UpdateTime": "2020-11-13T06:41:34.808Z",
                "CreateTime": "2020-11-13T06:41:34.808Z",
                "CoverUrl": "",
                "MediaCastProjectInfo": null,
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
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5c"
    }
}
```

**Example 3: 获取点播转直播项目信息**

 

Input: 

```
tccli cme DescribeProjects --cli-unfold-argument  \
    --Platform test \
    --CategorySet MEDIA_CAST \
    --ProjectIds cmepid_60599df66a6b440001518169
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectInfoSet": [
            {
                "ProjectId": "cmepid_60599df66a6b440001518169",
                "Name": "test",
                "AspectRatio": "",
                "Category": "MEDIA_CAST",
                "Owner": {
                    "Type": "PERSON",
                    "Id": "user_31345df76a6b44104571916a"
                },
                "UpdateTime": "2020-11-13T06:41:34.808Z",
                "CreateTime": "2020-11-13T06:41:34.808Z",
                "CoverUrl": "",
                "StreamConnectProjectInfo": null,
                "MediaCastProjectInfo": {
                    "Status": "Working",
                    "StartTime": "2020-11-13T06:41:34.808Z",
                    "StopTime": "2020-11-14T06:41:34.808Z",
                    "SourceInfos": [
                        {
                            "Id": "fsdf",
                            "Type": "CME",
                            "MaterialId": "a123"
                        },
                        {
                            "Id": "sdfs",
                            "Type": "VOD",
                            "FileId": "53434"
                        }
                    ],
                    "DestinationInfos": [
                        {
                            "Id": "2342342",
                            "Name": "test",
                            "PushUrl": "rtmp://livepush.video-studio.myqcloud.com/output/1250000001-600e8e66194ef500012d9b08"
                        }
                    ],
                    "PlaySetting": {
                        "LoopCount": 2
                    },
                    "OutputMediaSetting": {
                        "VideoSetting": {
                            "Width": 1920,
                            "Height": 1080,
                            "Bitrate": 2500,
                            "FrameRate": 25
                        }
                    }
                }
            }
        ],
        "RequestId": "c44cbb5b-b809-4061-8c45-7469b64e8e5c"
    }
}
```

