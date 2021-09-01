**Example 1: Sample request**



Input: 

```
tccli mdp CreateMediaPackageChannel --cli-unfold-argument  \
    --Name xxx \
    --Protocol HLS
```

Output: 
```
{
    "Response": {
        "Info": {
            "Id": "AEABF123954",
            "Name": "channelName",
            "Protocol": "HLS",
            "Points": {
                "Inputs": [
                    {
                        "Url": "http://mediapackage.${region}-1.srclivepush.myqcloud.com/v1/017182d5d3c4647d244530760443/017182d5d3c4647d244530760444",
                        "AuthInfo": {
                            "Username": "",
                            "Password": ""
                        }
                    },
                    {
                        "Url": "http://mediapackage.${region}-2.srclivepush.myqcloud.com/v1/017182d5d3c4647d244530760443/017182d5d3c4647d244530760445",
                        "AuthInfo": {
                            "Username": "",
                            "Password": ""
                        }
                    }
                ],
                "Endpoints": []
            }
        },
        "RequestId": "11-222-333"
    }
}
```

