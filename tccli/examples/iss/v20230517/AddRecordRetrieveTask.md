**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordRetrieveTask --cli-unfold-argument  \
    --TaskName name \
    --Describe  \
    --StartTime 1687688595 \
    --EndTime 1687692195 \
    --Mode 1 \
    --Expiration 3 \
    --Channels.0.DeviceId 64505f15-67b1-****-****-0ad6c8ce6aef \
    --Channels.0.ChannelId 0001a415-b9c1-****-****-b13cfb96c778
```

Output: 
```
{
    "Response": {}
}
```

