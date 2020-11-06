**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveChannelOutputStatistics --cli-unfold-argument  \
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
                "OutputGroupName": "TEST",
                "Statistics": {
                    "Pipeline0": [
                        {
                            "Timestamp": 1585554600,
                            "NetworkOut": 2000000
                        }
                    ],
                    "Pipeline1": [
                        {
                            "Timestamp": 1585554600,
                            "NetworkOut": 2000000
                        }
                    ]
                }
            }
        ],
        "RequestId": "11-222-222"
    }
}
```

