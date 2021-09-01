**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDomainPlayInfoList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DomainInfoList": [
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 309.998,
                        "Flux": 18599.88,
                        "MainlandOrOversea": "Mainland",
                        "Online": 374,
                        "Request": 175
                    },
                    {
                        "Bandwidth": 0,
                        "Flux": 0,
                        "MainlandOrOversea": "Oversea",
                        "Online": 0,
                        "Request": 0
                    }
                ],
                "Domain": "345.tencent.com"
            },
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 134351.765,
                        "Flux": 8061105.9,
                        "MainlandOrOversea": "Mainland",
                        "Online": 130171,
                        "Request": 102524
                    },
                    {
                        "Bandwidth": 0,
                        "Flux": 0,
                        "MainlandOrOversea": "Oversea",
                        "Online": 0,
                        "Request": 0
                    }
                ],
                "Domain": "123.tencent.com"
            }
        ],
        "RequestId": "04b76ebd-487d-4a7a-aca8-82060359feee",
        "Time": "2019-04-07 21:55:00",
        "TotalBandwidth": 2909181.92,
        "TotalFlux": 174550915.2,
        "TotalOnline": 2800396,
        "TotalRequest": 2446274
    }
}
```

