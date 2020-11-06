**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveChannelInputStatistics --cli-unfold-argument  \
    --ChannelId AEAE83719CE \
    --StartTime 2020-01-01T12:00:00Z \
    --EndTime 2020-01-01T14:00:00Z
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "InputId": "1111",
                "Statistics": {
                    "Pipeline0": [
                        {
                            "Timestamp": 1585554600,
                            "NetworkIn": 1500000,
                            "Video": [
                                {
                                    "Fps": 30,
                                    "Rate": 1500,
                                    "Pid": 256
                                }
                            ],
                            "Audio": [
                                {
                                    "Fps": 30,
                                    "Rate": 1500,
                                    "Pid": 256
                                }
                            ]
                        }
                    ],
                    "Pipeline1": [
                        {
                            "Timestamp": 1585554600,
                            "NetworkIn": 1500000,
                            "Video": [
                                {
                                    "Fps": 30,
                                    "Rate": 1500,
                                    "Pid": 256
                                }
                            ],
                            "Audio": [
                                {
                                    "Fps": 30,
                                    "Rate": 1500,
                                    "Pid": 256
                                }
                            ]
                        }
                    ]
                }
            }
        ],
        "RequestId": "11-222-222"
    }
}
```

