**Example 1: 获取账号调用记录列表**



Input: 

```
tccli csip DescribeUserCallRecord --cli-unfold-argument  \
    --SubUin 100021372635 \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppID": 10001,
                "CallCount": 5941,
                "Code": 0,
                "Date": "",
                "EventType": 1,
                "FirstCallTime": "2025-05-16 00:01:44",
                "ISP": "腾讯云",
                "LastCallTime": "2025-05-22 11:09:39",
                "Region": "中国-广东省-广州市",
                "SourceIP": "106.55.***.47",
                "SourceIPRemark": "",
                "UserName": "name"
            }
        ],
        "RequestId": "502c625d-756e-4bdb-bd5f-784d008150b5",
        "Total": 1
    }
}
```

