**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveChannelAlerts --cli-unfold-argument  \
    --ChannelId 1111
```

Output: 
```
{
    "Response": {
        "Infos": {
            "Pipeline0": [
                {
                    "SetTime": "2020-03-30T07:04:08Z",
                    "ClearTime": "2020-03-30T08:04:08Z",
                    "Type": "RTMP Stream Not Found",
                    "Message": "Searching for RTMP Push stream [testStream], which does not exist at this time"
                }
            ],
            "Pipeline1": [
                {
                    "SetTime": "2020-03-30T07:04:08Z",
                    "ClearTime": "2020-03-30T08:04:08Z",
                    "Type": "Failed to Wtite to Output",
                    "Message": "Failed to send file for URL [http://www.domain2.com/live/index.m3u8], after [3] attempts, error [http client error [405]]"
                }
            ]
        },
        "RequestId": "11-222-222"
    }
}
```

