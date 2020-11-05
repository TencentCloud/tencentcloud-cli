**Example 1: Sample request**



Input: 

```
tccli live DescribeDeliverBandwidthList --cli-unfold-argument  \
    --StartTime '2020-01-07 21:10:00'\
    --EndTime '2020-01-07 21:15:00'
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Bandwidth": 45927.6,
                "Time": "2020-05-01 00:00:00"
            },
            {
                "Bandwidth": 44494.84,
                "Time": "2020-05-01 00:05:00"
            },
            {
                "Bandwidth": 43061.09,
                "Time": "2020-05-01 00:10:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

