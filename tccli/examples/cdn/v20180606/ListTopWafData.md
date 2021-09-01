**Example 1: 获取Waf攻击Top数据**



Input: 

```
tccli cdn ListTopWafData --cli-unfold-argument  \
    --Domain www.test.com \
    --StartTime 2019-06-2600:00:00 \
    --EndTime 2019-06-2603:00:00 \
    --Metric url
```

Output: 
```
{
    "Response": {
        "RequestId": "4f1bb066-524f-4857-87f4-0ae56439179b",
        "TopTypeData": [
            {
                "AttackType": "xss",
                "Value": 20
            },
            {
                "AttackType": "sql",
                "Value": 831
            }
        ],
        "TopIpData": [
            {
                "Time": "2019-06-26 05:42:00",
                "Value": 18,
                "District": "江苏",
                "Isp": "中国电信",
                "Ip": "222.186.20.85"
            }
        ],
        "TopUrlData": [
            {
                "Time": "2019-06-26 05:42:00",
                "Value": 18,
                "Domain": "www.test.com",
                "Url": "/path"
            }
        ],
        "TopDomainData": [
            {
                "Value": 18,
                "Percent": 0.0,
                "Domain": "www.test.com"
            },
            {
                "Value": 9,
                "Percent": 0.0,
                "Domain": "www.123.com"
            }
        ]
    }
}
```

