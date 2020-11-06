**Example 1: 获取CC的IP黑白名单**



Input: 

```
tccli dayu DescribeCCIpAllowDeny --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Type black \
    --Protocol http
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "white",
                "Value": "123.20.10.0/24,1.1.11.1"
            },
            {
                "Key": "total",
                "Value": "2"
            }
        ],
        "RecordList": [
            {
                "Record": [
                    {
                        "Key": "ip",
                        "Value": "123.20.10.0/24"
                    },
                    {
                        "Key": "domain",
                        "Value": ""
                    },
                    {
                        "Key": "protocol",
                        "Value": "http"
                    },
                    {
                        "Key": "type",
                        "Value": "white"
                    }
                ]
            },
            {
                "Record": [
                    {
                        "Key": "ip",
                        "Value": "1.1.11.1"
                    },
                    {
                        "Key": "domain",
                        "Value": ""
                    },
                    {
                        "Key": "protocol",
                        "Value": "http"
                    },
                    {
                        "Key": "type",
                        "Value": "white"
                    }
                ]
            }
        ],
        "RequestId": "40fc168e-a7c1-4bdc-92b9-d5b3f88369a9",
        "Total": 2
    }
}
```

