**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveInputs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Info": [
            {
                "Id": "2",
                "Name": "a",
                "Type": "RTMP_PUSH",
                "SecurityGroupIds": [
                    "sss"
                ],
                "AttachedChannels": [
                    "ccc"
                ],
                "InputSettings": [
                    {
                        "InputAddress": "rtmp://1.mdialive.ap-xxx.livepush.myqcloud.com",
                        "AppName": "live",
                        "StreamName": "streamA",
                        "SourceUrl": ""
                    },
                    {
                        "InputAddress": "rtmp://1.mdialive.ap-xxx.livepush.myqcloud.com",
                        "AppName": "live",
                        "StreamName": "streamB",
                        "SourceUrl": ""
                    }
                ]
            },
            {
                "Id": "2",
                "Name": "a",
                "Type": "RTMP_PUSH",
                "SecurityGroupIds": [
                    "sss"
                ],
                "AttachedChannels": [
                    "ccc2"
                ],
                "InputSettings": [
                    {
                        "InputAddress": "rtmp://1.mdialive.ap-xxx.livepush.myqcloud.com",
                        "AppName": "live",
                        "StreamName": "streamC",
                        "SourceUrl": ""
                    },
                    {
                        "InputAddress": "rtmp://1.mdialive.ap-xxx.livepush.myqcloud.com",
                        "AppName": "live",
                        "StreamName": "streamD",
                        "SourceUrl": ""
                    }
                ]
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

