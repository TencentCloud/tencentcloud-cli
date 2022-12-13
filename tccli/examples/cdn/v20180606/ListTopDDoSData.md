**Example 1: 获取DDoS攻击Top数据**



Input: 

```
tccli cdn ListTopDDoSData --cli-unfold-argument  \
    --EndTime 2020-09-22 01:00:00 \
    --StartTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "123456",
        "Data": [
            {
                "Value": 1,
                "AttackType": "ddos"
            }
        ],
        "IPData": [
            {
                "Province": "广东省",
                "Country": "中国",
                "Isp": "中国电信",
                "AttackCount": 100,
                "AttackIP": "10.32.1.3"
            }
        ]
    }
}
```

