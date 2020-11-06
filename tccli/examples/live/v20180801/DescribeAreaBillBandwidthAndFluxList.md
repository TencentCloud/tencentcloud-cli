**Example 1: Sample request**



Input: 

```
tccli live DescribeAreaBillBandwidthAndFluxList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com \
    --StartTime 2019-02-0100:00:00 \
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
                "Name": "Middle East/Africa",
                "Countrys": [
                    {
                        "Name": "United Arab Emirates",
                        "BandInfoList": [
                            {
                                "Bandwidth": 6.95,
                                "Flux": 260.7,
                                "PeakTime": "2020-09-09 00:00:00",
                                "Time": "2020-09-09 00:05:00"
                            },
                            {
                                "Bandwidth": 5.84,
                                "Flux": 219.09,
                                "PeakTime": "2020-09-09 00:05:00",
                                "Time": "2020-09-09 00:10:00"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

