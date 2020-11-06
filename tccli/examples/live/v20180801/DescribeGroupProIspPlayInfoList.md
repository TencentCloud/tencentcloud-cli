**Example 1: Sample request**

District/ISP [mapping table](/document/api/267/34019).

Input: 

```
tccli live DescribeGroupProIspPlayInfoList --cli-unfold-argument  \
    --StartTime '2019-03-29 09:00:00' \
    --EndTime '2019-03-29 09:10:00'
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 863.073,
                        "Flux": 6473.05,
                        "Online": 540,
                        "Request": 449,
                        "Time": "2019-03-29 09:00:00"
                    },
                    {
                        "Bandwidth": 891.49,
                        "Flux": 6686.173,
                        "Online": 524,
                        "Request": 455,
                        "Time": "2019-03-29 09:05:00"
                    },
                    {
                        "Bandwidth": 847.715,
                        "Flux": 6357.859,
                        "Online": 612,
                        "Request": 578,
                        "Time": "2019-03-29 09:10:00"
                    }
                ],
                "IspName": "China Telecom",
                "ProvinceName": "Guangdong"
            },
            {
                "DetailInfoList": [
                    {
                        "Bandwidth": 213.405,
                        "Flux": 1600.537,
                        "Online": 132,
                        "Request": 184,
                        "Time": "2019-03-29 09:00:00"
                    },
                    {
                        "Bandwidth": 215.738,
                        "Flux": 1618.032,
                        "Online": 125,
                        "Request": 122,
                        "Time": "2019-03-29 09:05:00"
                    },
                    {
                        "Bandwidth": 226.96,
                        "Flux": 1702.203,
                        "Online": 131,
                        "Request": 131,
                        "Time": "2019-03-29 09:10:00"
                    }
                ],
                "IspName": "China Unicom",
                "ProvinceName": "Guangdong"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

