**Example 1: 无录像时间段**

 

Input: 

```
tccli iss DescribeRecordFile --cli-unfold-argument  \
    --DeviceId 389708b2-bcbb-****-****-a61f528b2a15 \
    --ChannelId 32525dd7-c3fc-****-****-d5beb4acd1e1 \
    --StartTime 1687622400 \
    --EndTime 1687708799
```

Output: 
```
{
    "Response": {}
}
```

**Example 2: 有录像时间段**

 

Input: 

```
tccli iss DescribeRecordFile --cli-unfold-argument  \
    --DeviceId 389708b2-bcbb-****-****-a61f528b2a15 \
    --ChannelId 32525dd7-c3fc-****-****-d5beb4acd1e1 \
    --StartTime 1687622400 \
    --EndTime 1687708799
```

Output: 
```
{
    "Response": {}
}
```

