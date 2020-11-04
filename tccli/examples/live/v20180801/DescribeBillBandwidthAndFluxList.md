**Example 1: 请求示例**



Input: 

```
tccli live DescribeBillBandwidthAndFluxList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com\
    --StartTime 2019-02-0100:00:00\
    --EndTime 2019-02-0100:10:00
```

Output: 
```
{
    "Response": {
        "95PeakBandwidth": 117042.495,
        "95PeakBandwidthTime": "2019-02-01 00:00:00",
        "DataInfoList": [
            {
                "Bandwidth": 117042.495,
                "Flux": 4389093.551,
                "Time": "2019-02-01 00:00:00",
                "PeakTime": "2019-02-01 00:00:00"
            },
            {
                "Bandwidth": 110364.995,
                "Flux": 4138687.32,
                "Time": "2019-02-01 00:05:00",
                "PeakTime": "2019-02-01 00:05:00"
            },
            {
                "Bandwidth": 99380.978,
                "Flux": 3726786.679,
                "Time": "2019-02-01 00:10:00",
                "PeakTime": "2019-02-01 00:10:00"
            }
        ],
        "PeakBandwidth": 117042.495,
        "PeakBandwidthTime": "2019-02-01 00:00:00",
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec",
        "SumFlux": 12254567.55
    }
}
```

