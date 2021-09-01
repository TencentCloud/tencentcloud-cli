**Example 1: 安全加速CC攻击Top N数据查询**



Input: 

```
tccli cdn ListTopCcData --cli-unfold-argument  \
    --Domain www.test.com \
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
                "Ip": "1.1.1.1",
                "Url": "/test.html?key=value",
                "UserAgent": "",
                "Value": 1000,
                "Domain": "123.com"
            },
            {
                "Ip": "2.2.2.2",
                "Url": "/test.html",
                "UserAgent": "",
                "Value": 900,
                "Domain": "123.com"
            }
        ]
    }
}
```

