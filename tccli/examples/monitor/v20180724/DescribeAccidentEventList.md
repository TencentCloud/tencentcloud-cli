**Example 1: Getting the platform event list**

This example shows you how to get the platform event list.

Input: 

```
tccli monitor DescribeAccidentEventList --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "Data": {
            "Alarms": [
                {
                    "OccurTime": "2019-10-10T15:03:31+08:00",
                    "AccidentType": 23,
                    "BusinessID": 1,
                    "AffectResource": "ins-19708ino",
                    "EventStatus": 0,
                    "Region": "gz",
                    "UpdateTime": "2019-10-10T15:03:31+08:00",
                    "AccidentTypeDesc": "CVM run exception",
                    "BusinessTypeDesc": "Service error"
                }
            ],
            "Total": 1
        },
        "RequestId": "test813c-45d8-459a-8978-aaasahuiaa"
    }
}
```

