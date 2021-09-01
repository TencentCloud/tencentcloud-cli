**Example 1: Sample request**



Input: 

```
tccli mdp CreateMediaPackageChannelEndpoint --cli-unfold-argument  \
    --Id XXX \
    --Name XXX \
    --AuthInfo.WhiteIpList 0.0.0.0/0 \
    --AuthInfo.BlackIpList 0.0.0.0/0 \
    --AuthInfo.AuthKey XXX
```

Output: 
```
{
    "Response": {
        "RequestId": "11-222-333",
        "Info": {
            "Name": "",
            "Url": "",
            "AuthInfo": {
                "WhiteIpList:": [
                    "1.2.3.4/24",
                    "19.76.68.1/1"
                ],
                "BlackIpList:": [
                    "1.2.3.4/24",
                    "19.76.68.1/1"
                ],
                "AuthKey": ""
            }
        }
    }
}
```

