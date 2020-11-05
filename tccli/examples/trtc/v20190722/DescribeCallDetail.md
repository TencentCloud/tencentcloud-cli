**Example 1: Querying user list and call metrics**



Input: 

```
tccli trtc DescribeCallDetail --cli-unfold-argument  \
    --CommId 1400353843_218695_1590065777\
    --StartTime 1590065777\
    --EndTime 1590065877\
    --SdkAppId 1400353843\
    --DataType bigvCapFps
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "UserList": [
            {
                "RoomStr": "218695",
                "UserId": "1716",
                "JoinTs": 1590065777,
                "LeaveTs": 1590067658,
                "Finished": true,
                "DeviceType": "",
                "SdkVersion": "4.3.14",
                "ClientIp": "10.4.1.13"
            }
        ],
        "Data": [
            {
                "Content": [
                    {
                        "Time": 1590065779,
                        "Value": 0
                    },
                    {
                        "Time": 1590065781,
                        "Value": 0
                    },
                    {
                        "Time": 1590065783,
                        "Value": 0
                    },
                    {
                        "Time": 1590065785,
                        "Value": 0
                    },
                    {
                        "Time": 1590065787,
                        "Value": 0
                    },
                    {
                        "Time": 1590065789,
                        "Value": 0
                    },
                    {
                        "Time": 1590065791,
                        "Value": 0
                    },
                    {
                        "Time": 1590065793,
                        "Value": 0
                    },
                    {
                        "Time": 1590065795,
                        "Value": 0
                    },
                    {
                        "Time": 1590065797,
                        "Value": 0
                    },
                    {
                        "Time": 1590065799,
                        "Value": 0
                    },
                    {
                        "Time": 1590065801,
                        "Value": 0
                    },
                    {
                        "Time": 1590065803,
                        "Value": 0
                    },
                    {
                        "Time": 1590065805,
                        "Value": 0
                    },
                    {
                        "Time": 1590065807,
                        "Value": 0
                    },
                    {
                        "Time": 1590065809,
                        "Value": 0
                    },
                    {
                        "Time": 1590065811,
                        "Value": 0
                    },
                    {
                        "Time": 1590065813,
                        "Value": 0
                    },
                    {
                        "Time": 1590065815,
                        "Value": 0
                    },
                    {
                        "Time": 1590065817,
                        "Value": 0
                    },
                    {
                        "Time": 1590065819,
                        "Value": 0
                    },
                    {
                        "Time": 1590065821,
                        "Value": 0
                    },
                    {
                        "Time": 1590065823,
                        "Value": 0
                    },
                    {
                        "Time": 1590065825,
                        "Value": 0
                    },
                    {
                        "Time": 1590065827,
                        "Value": 0
                    },
                    {
                        "Time": 1590065829,
                        "Value": 0
                    },
                    {
                        "Time": 1590065831,
                        "Value": 0
                    },
                    {
                        "Time": 1590065833,
                        "Value": 0
                    },
                    {
                        "Time": 1590065835,
                        "Value": 0
                    },
                    {
                        "Time": 1590065837,
                        "Value": 0
                    },
                    {
                        "Time": 1590065839,
                        "Value": 0
                    },
                    {
                        "Time": 1590065841,
                        "Value": 0
                    },
                    {
                        "Time": 1590065843,
                        "Value": 0
                    },
                    {
                        "Time": 1590065845,
                        "Value": 0
                    },
                    {
                        "Time": 1590065847,
                        "Value": 0
                    },
                    {
                        "Time": 1590065849,
                        "Value": 0
                    },
                    {
                        "Time": 1590065851,
                        "Value": 0
                    },
                    {
                        "Time": 1590065853,
                        "Value": 0
                    },
                    {
                        "Time": 1590065855,
                        "Value": 0
                    },
                    {
                        "Time": 1590065857,
                        "Value": 0
                    },
                    {
                        "Time": 1590065859,
                        "Value": 0
                    },
                    {
                        "Time": 1590065861,
                        "Value": 0
                    },
                    {
                        "Time": 1590065863,
                        "Value": 0
                    },
                    {
                        "Time": 1590065865,
                        "Value": 0
                    },
                    {
                        "Time": 1590065867,
                        "Value": 0
                    },
                    {
                        "Time": 1590065869,
                        "Value": 0
                    },
                    {
                        "Time": 1590065871,
                        "Value": 0
                    },
                    {
                        "Time": 1590065873,
                        "Value": 0
                    },
                    {
                        "Time": 1590065875,
                        "Value": 0
                    },
                    {
                        "Time": 1590065877,
                        "Value": 0
                    }
                ],
                "PeerId": "",
                "UserId": "1716",
                "DataType": "bigvCapFps"
            }
        ],
        "RequestId": "2e12e365-43e8-4efd-902d-906303e2ee4a"
    }
}
```

