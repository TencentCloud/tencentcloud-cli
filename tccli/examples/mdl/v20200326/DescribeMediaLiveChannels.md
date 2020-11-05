**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveChannels --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Region": "ap-guangzhou",
                "Id": "5E95AB6430E630731B8B",
                "Name": "555",
                "State": "IDLE",
                "AttachedInputs": [
                    {
                        "Id": "5E8EEA7B30E6131D85CB",
                        "AudioSelectors": [
                            {
                                "Name": "7777",
                                "AudioPidSelection": {
                                    "Pid": 888
                                }
                            }
                        ]
                    }
                ],
                "AudioTemplates": [
                    {
                        "Name": "test1",
                        "Acodec": "AAC",
                        "AudioBitrate": 6000,
                        "AudioSelectorName": "7777",
                        "LanguageCode": "eng"
                    }
                ],
                "VideoTemplates": [
                    {
                        "Name": "test2",
                        "Vcodec": "H264",
                        "VideoBitrate": 1000000,
                        "Width": 1024,
                        "Height": 1024,
                        "Gop": 2,
                        "Fps": 30
                    }
                ],
                "OutputGroups": [
                    {
                        "Name": "9999",
                        "RemuxProtocol": "DASH",
                        "HlsRemuxSettings": {
                            "SegmentDuration": 0,
                            "SegmentNumber": 0,
                            "PdtInsertion": "CLOSE",
                            "PdtDuration": 0
                        },
                        "DashRemuxSettings": {
                            "SegmentDuration": 2000,
                            "SegmentNumber": 3,
                            "PeriodTriggers": "OPEN"
                        },
                        "DrmSettings": {
                            "State": "OPEN",
                            "ContentId": "f28d75a5-d386-4c5c-acce-779b4896cf0d"
                        },
                        "Outputs": [
                            {
                                "Name": "11111122222",
                                "AudioTemplateNames": [
                                    "test1"
                                ],
                                "VideoTemplateNames": [
                                    "test2"
                                ],
                                "Scte35Settings": {
                                    "Behavior": "PASSTHROUGH"
                                }
                            }
                        ],
                        "Destinations": [
                            {
                                "OutputUrl": "http://domain/live/1233",
                                "AuthKey": "2323",
                                "Username": "24343",
                                "Password": ""
                            },
                            {
                                "OutputUrl": "http://domain/live/222",
                                "AuthKey": "dsds",
                                "Username": "443",
                                "Password": "666"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "11-222-333"
    }
}
```

