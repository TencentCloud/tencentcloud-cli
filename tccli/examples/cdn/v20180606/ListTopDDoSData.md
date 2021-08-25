**Example 1: 获取DDoS攻击Top数据**



Input: 

```
tccli cdn ListTopDDoSData --cli-unfold-argument  \
    --StartTime '2020-09-22 00:00:00' \
    --EndTime '2020-09-22 01:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "123456",
        "Data": [
            {
                "AttackType": "UDP Flood",
                "Value": 10
            },
            {
                "AttackType": "TCP Flood",
                "Value": 2
            }
        ]
    }
}
```

