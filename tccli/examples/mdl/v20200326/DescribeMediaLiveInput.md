**Example 1: Sample request**



Input: 

```
tccli mdl DescribeMediaLiveInput --cli-unfold-argument  \
    --Id 1111
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": "2",
            "Name": "a",
            "Type": "RTMP_PUSH",
            "SecurityGroupIds": [
                "sss"
            ],
            "AttachedChannels": null,
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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

