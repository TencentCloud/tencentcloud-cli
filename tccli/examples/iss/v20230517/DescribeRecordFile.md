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
    "Response": {
        "Data": {
            "List": null,
            "Tips": 0
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
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
    "Response": {
        "Data": {
            "Tips": 0,
            "List": [
                {
                    "Begin": 1687651516,
                    "End": 1687653336
                },
                {
                    "Begin": 1687653336,
                    "End": 1687655156
                },
                {
                    "Begin": 1687655156,
                    "End": 1687656976
                },
                {
                    "Begin": 1687656976,
                    "End": 1687658796
                }
            ]
        },
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

