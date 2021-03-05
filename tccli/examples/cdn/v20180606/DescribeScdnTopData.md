**Example 1: 获取SCDN的Top数据**



Input: 

```
tccli cdn DescribeScdnTopData --cli-unfold-argument  \
    --Domain www.test.com \
    --Mode waf \
    --Filter request \
    --Metric url \
    --StartTime 2019-06-2600:00:00 \
    --EndTime 2019-06-2603:00:00
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
                "Time": "2019-06-26 05:42:56",
                "Value": 18,
                "Isp": "中国电信",
                "Ip": "222.186.20.85"
            }
        ],
        "Mode": "waf"
    }
}
```

