**Example 1: 获取CC的URL白名单**



Input: 

```
tccli dayu DescribeCCUrlAllow --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --Type white \
    --Protocol http
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "whiteurllist",
                "Value": ""
            },
            {
                "Key": "whitetotal",
                "Value": "1"
            }
        ],
        "RecordList": [
            {
                "Record": [
                    {
                        "Key": "url",
                        "Value": "http://2.2.2.2/test.html"
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
        "RequestId": "6084150e-f2f7-4024-8821-a51fe7115ea0",
        "Total": 1
    }
}
```

