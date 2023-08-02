**Example 1: 成功**

 

Input: 

```
tccli iss ControlDevicePreset --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890abcd \
    --Cmd set \
    --Index 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4ebd45e0-9434-4917-a5eb-78879f545d9b"
    }
}
```

