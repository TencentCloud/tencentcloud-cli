**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveChannelLogs --cli-unfold-argument  \
    --ChannelId AEAE83719CE \
    --StartTime 2020-01-01T12:00:00Z \
    --EndTime 2020-01-01T14:00:00Z
```

Output: 
```
{
    "Response": {
        "Infos": {
            "Pipeline0": [
                {
                    "Type": "StreamStart",
                    "Time": "2020-07-07T04:07:40Z",
                    "Message": {
                        "StreamInfo": {
                            "ClientIp": "1.1.1.1",
                            "Video": [
                                {
                                    "Pid": 256,
                                    "Codec": "H264",
                                    "Fps": 0,
                                    "Rate": 0,
                                    "Width": 0,
                                    "Height": 0
                                }
                            ],
                            "Audio": [
                                {
                                    "Pid": 257,
                                    "Codec": "",
                                    "Fps": 0,
                                    "Rate": 0,
                                    "SampleRate": 0
                                }
                            ],
                            "Scte35": [
                                {
                                    "Pid": 0
                                }
                            ]
                        }
                    }
                }
            ],
            "Pipeline1": []
        },
        "RequestId": "85c76051-d775-4a88-84fa-a9a51c1cfd97"
    }
}
```

