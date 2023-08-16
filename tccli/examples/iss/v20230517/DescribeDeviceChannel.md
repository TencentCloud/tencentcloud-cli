**Example 1: 成功**

 

Input: 

```
tccli iss DescribeDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ChannelCode": "02Bu9VFOfl",
                "ChannelId": "02Bu9VFOfl",
                "DeviceId": "12345678-abcd-efgh-ijkl-1234567890abcd",
                "Manufacturer": "",
                "Name": "rtmp10087",
                "PTZType": 0,
                "Resolution": "",
                "State": 0,
                "Status": 0
            }
        ],
        "RequestId": "4c660931-4027-4ae0-a6ac-18530005d8f1"
    }
}
```

**Example 2: 设备不存在**

 

Input: 

```
tccli iss DescribeDeviceChannel --cli-unfold-argument  \
    --DeviceId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "该资源不存在"
        },
        "RequestId": "30b56ca7-1de0-4d1e-ac87-2dcc2fbd08e5"
    }
}
```

