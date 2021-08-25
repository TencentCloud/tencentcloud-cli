**Example 1: 查询bot的topN域名**



Input: 

```
tccli cdn ListTopBotData --cli-unfold-argument  \
    --TopCount 10 \
    --StartTime '2020-04-20 12:00:00' \
    --EndTime '2020-04-20 23:59:00'
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Domain": "zc-work.qcloudwaf.com",
                "Count": 1,
                "Value": "",
                "Isp": "xx",
                "Province": "",
                "Country": ""
            }
        ],
        "RequestId": "requestid0000000"
    }
}
```

