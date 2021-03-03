**Example 1: 查询执行的事件历史**



Input: 

```
tccli asw DescribeExecutionHistory --cli-unfold-argument  \
    --ExecutionResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 1,
                "EventCategory": "ExecutionStart",
                "StepName": "START",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{\"input\":\"{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"}\",\"role\":\"qrn:qcs:asw:sh:1300074211:http:qrn\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 2,
                "EventCategory": "Unknown",
                "StepName": "START",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "null",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 3,
                "EventCategory": "PassNodeEnter",
                "StepName": "ReceivedVideo",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{\"input\":\"{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"}\",\"local_variables\":\"{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 4,
                "EventCategory": "PassNodeExit",
                "StepName": "ReceivedVideo",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{\"output\":\"{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"}\",\"exception\":{},\"local_variables\":\"{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"}\",\"next\":\"[\"MPSAudioSeparate\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 5,
                "EventCategory": "TaskNodeEnter",
                "StepName": "MPSAudioSeparate",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:audioSeparate",
                "Timestamp": "1596716960311",
                "Content": "{\"input\":\"{\"InputInfo\":{\"CosInputInfo\":{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"},\"Type\":\"COS\"},\"MediaProcessTask\":{\"TranscodeTaskSet\":[{\"Definition\":0,\"RawParameter\":{\"AudioTemplate\":{\"AudioChannel\":2,\"Bitrate\":0,\"Codec\":\"libmp3lame\",\"SampleRate\":32000},\"Container\":\"mp3\",\"RemoveAudio\":0,\"RemoveVideo\":1}}]}}\",\"local_variables\":\"{\"InputInfo\":{\"CosInputInfo\":{\"Bucket\":\"bilibili-1300074211\",\"Object\":\"demo1.mp4\",\"Region\":\"ap-shanghai\"},\"Type\":\"COS\"},\"MediaProcessTask\":{\"TranscodeTaskSet\":[{\"Definition\":0,\"RawParameter\":{\"AudioTemplate\":{\"AudioChannel\":2,\"Bitrate\":0,\"Codec\":\"libmp3lame\",\"SampleRate\":32000},\"Container\":\"mp3\",\"RemoveAudio\":0,\"RemoveVideo\":1}}]}}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 6,
                "EventCategory": "TaskNodeExit",
                "StepName": "MPSAudioSeparate",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:audioSeparate",
                "Timestamp": "1596716960514",
                "Content": "{\"output\":\"{\"Response\":{\"RequestId\":\"14161bbf-334d-431e-819d-6646640f432c\",\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}}\",\"exception\":{},\"local_variables\":\"{\"Response\":{\"RequestId\":\"14161bbf-334d-431e-819d-6646640f432c\",\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}}\",\"next\":\"[\"CheckMPS\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 7,
                "EventCategory": "TaskNodeEnter",
                "StepName": "CheckMPS",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:checkMpsJob",
                "Timestamp": "1596716960514",
                "Content": "{\"input\":\"{\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}\",\"local_variables\":\"{\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 8,
                "EventCategory": "TaskNodeExit",
                "StepName": "CheckMPS",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:checkMpsJob",
                "Timestamp": "1596716993478",
                "Content": "{\"output\":\"{\"Response\":{\"BeginProcessTime\":\"2020-08-06T12:30:13Z\",\"CreateTime\":\"2020-08-06T12:30:12Z\",\"FinishTime\":\"2020-08-06T12:30:42Z\",\"RequestId\":\"f65fa285-7230-439e-bbe1-b8ef3bdb8128\",\"Sesegion\":\"ap-shanghai\"},\"Type\":\"COS\"},\"SegmentObjectName\":\"/demo1_transcode_0_{number}\"},\"Message\":\"SUCCESS\",\"Output\":{\"AudioStreamSet\":[{\"Bitrate\":128000,\"Codec\":\"mp3\",\"SamplingRate\":32000}],\"Bitrate\":128000,\"Container\":\"mp3\",\"Definition\":0,\"Duration\":186.804,\"Height\":0,\"Md5\":\"24a4eabdb816dbd00d82a9fa16e54e0d\",\"OutputStorage\":{\"CosOutputStorage\":{\"Bucket\":\"bilibili-1300074211\",\"Region\":\"ap-shanghai\"},\"Type\":\"COS\"},\"Path\":\"/demo1_transcode_0.mp3\",\"Size\":2989485,\"Width\":0},\"Status\":\"SUCCESS\"},\"Type\":\"Transcode\"}],\"Message\":\"\",\"MetaData\":{\"AudioDuration\":186.75216674804688,\"AudioStreamSet\":[{\"Bitrate\":128627,\"Codec\":\"aac\",\"SamplingRate\":48000}],\"Bitrate\":3051497,\"Container\":\"mov,mp4,m4a,3gp,3g2,mj2\",\"Duration\":186.75216674804688,\"Height\":1080,\"Rotate\":0,\"Size\":71349940,\"VideoDuration\":186.67999267578125,\"VideoStreamSet\":[{\"Bitrate\":2922870,\"Codec\":\"h264\",\"Fps\":25,\"Height\":1080,\"Width\":1920}],\"Width\":1920},\"Status\":\"FINISH\",\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}}}\",\"next\":\"[\"GetMPSAudioURL\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 9,
                "EventCategory": "TaskNodeEnter",
                "StepName": "GetMPSAudioURL",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:scf:Invoke/GetMPSAudioURL",
                "Timestamp": "1596716993481",
                "Content": "{\"inpu2:30:13Z\",\"CreateTime\":\"2020-08-06T12:30:12Z\",\"FinishTime\":\"2020-08-06T12:30:42Z\",\"RequestId\":\"f65fa285-7230-439e-bbe1-b8ef3bdb8128\",\"SessionContext\":otate\":0,\"Size\":71349940,\"VideoDuration\":186.67999267578125,\"VideoStreamSet\":[{\"Bitrate\":2922870,\"Codec\":\"h264\",\"Fps\":25,\"Height\":1080,\"Width\":1920}],\"Width\":1920},\"Status\":\"FINISH\",\"TaskId\":\"2500074211-WorkflowTask-3f4f0cc5527aebb82f09711e627c6704t0\"}}}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 10,
                "EventCategory": "TaskNodeExit",
                "StepName": "GetMPSAudioURL",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:scf:Invoke/GetMPSAudioURL",
                "Timestamp": "1596716993747",
                "Content": "{\"output\":\"{\"URL\":\"https://bilibili-1300074211.cos.ap-shanghai.myqcloud.com/demo1_transcode_0.mp3\"}\",\"exception\":{},\"local_variables\":\"{\"URL\":\"https://bilibili-1300074211.cos.ap-shanghai.myqcloud.com/demo1_transcode_0.mp3\"}\",\"next\":\"[\"ASR\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 11,
                "EventCategory": "TaskNodeEnter",
                "StepName": "ASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:generalASR",
                "Timestamp": "1596716993748",
                "Content": "{\"input\":\"{\"ChannelNum\":1,\"EngineModelType\":\"16k_zh\",\"ResTextFormat\":0,\"SourceType\":0,\"Url\":\"https://bilibili-1300074211.cos.ap-shanghai.myqcloud.com/demo1_transcode_0.mp3\"}\",\"local_variables\":\"{\"ChannelNum\":1,\"EngineModelType\":\"16k_zh\",\"ResTextFormat\":0,\"SourceType\":0,\"Url\":\"https://bilibili-1300074211.cos.ap-shanghai.myqcloud.com/demo1_transcode_0.mp3\"}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 12,
                "EventCategory": "TaskNodeExit",
                "StepName": "ASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:generalASR",
                "Timestamp": "1596716994159",
                "Content": "{\"output\":\"{\"Response\":{\"Data\":{\"TaskId\":852855024},\"RequestId\":\"2804633a-bf84-48cb-8805-2cafa231c881\"}}\",\"exception\":{},\"local_variables\":\"{\"Response\":{\"Data\":{\"TaskId\":852855024},\"RequestId\":\"2804633a-bf84-48cb-8805-2cafa231c881\"}}\",\"next\":\"[\"CheckASR\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 13,
                "EventCategory": "TaskNodeEnter",
                "StepName": "CheckASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:checkASR",
                "Timestamp": "1596716994160",
                "Content": "{\"input\":\"{\"TaskId\":852855024}\",\"local_variables\":\"{\"TaskId\":852855024}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 14,
                "EventCategory": "TaskNodeExit",
                "StepName": "CheckASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:checkASR",
                "Timestamp": "1596717016158",
                "Content": "{\"output\":\"{\"Response\":{\"Data\":{\"ErrorMsg\":\"\",\"Result\":\"[0:0.000,0:50.001]  Hello，大家好，我是大眼妆，同时也是一个适合肿眼泡的眼睛放大术，这次还用到了新买的桃子腮红这个妆容的重点就在于浓密纤长的睫毛，还有果汁版的唇妆不灵不灵的眼影呢，则是点睛之笔，感兴趣的话就继续看下去吧啊，苏岩好没精神，首先我的底妆还是惯例的好用，而且真的是荔枝为了更日系一点感觉不错，好啦，那么这次视频就结束啦，希望大家给我点个一健，三联，拜托，拜托，咱们下次见拜拜。n\",\"Status\":2,\"StatusStr\":\"success\",\"TaskId\":852855024},\"RequestId\":\"c5bca143-768a-4612-8a40-c891d7d08816\"}}\",\"next\":\"[\"END\"]\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:1300074211:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-bgi61kw1",
                "EventId": 15,
                "EventCategory": "Unknown",
                "StepName": "END",
                "ResourceName": "",
                "Timestamp": "1596717016159",
                "Content": "null",
                "Exception": ""
            }
        ],
        "RequestId": ""
    }
}
```

