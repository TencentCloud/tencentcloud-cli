**Example 1: 更新tpns信息**



Input: 

```
tccli im UpdateTPNSInfo --cli-unfold-argument  \
    --IMAccessId 140000100 \
    --TPNSAccessInfo.0.AccessId 1500085000 \
    --TPNSAccessInfo.0.SecretKey 0f17b7f09d7d6dcc05b37dc7c4330000 \
    --TPNSAccessInfo.0.Platform 15 \
    --TPNSAccessInfo.0.AccessKey A9C21C5ODCVE \
    --TPNSAccessInfo.0.ZoneUrl https://abc.com
```

Output: 
```
{
    "Response": {
        "TPNSUpdateRes": [
            {
                "AccessId": 1500085000,
                "SecretKey": "0f17b7f09d7d6dcc05b37dc7c4330000",
                "Platform": 15,
                "AccessKey": "A9C21C5ODCVE",
                "ErrorCode": 0,
                "ErrorMessage": "ok",
                "ZoneUrl": "https://abc.com"
            }
        ],
        "RequestId": "e171fe05-990b-4f49-8111-8xb34ee957944"
    }
}
```

