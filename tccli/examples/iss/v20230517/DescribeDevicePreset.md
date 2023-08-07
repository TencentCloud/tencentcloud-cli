**Example 1: 成功**

 

Input: 

```
tccli iss DescribeDevicePreset --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Index": 1,
                "Name": "abc"
            }
        ],
        "RequestId": "31facf8f-d783-4c28-a27f-82757eb71244"
    }
}
```

