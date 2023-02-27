**Example 1: 查询bot的topN域名**

查询bot的topN域名

Input: 

```
tccli cdn ListScdnTopBotData --cli-unfold-argument  \
    --TopCount 10 \
    --StartTime '2020-04-20 12:00:00' \
    --EndTime '2020-04-20 23:59:00' \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 1,
                "Value": "110.242.68.66",
                "Province": "广东",
                "Country": "中国",
                "Isp": "电信"
            }
        ],
        "RequestId": "requestid0000000"
    }
}
```

