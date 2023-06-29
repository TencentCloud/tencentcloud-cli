**Example 1: 更新tpns信息**



Input: 

```
tccli im UpdateTPNSInfo --cli-unfold-argument  \
    --IMAccessId 140000100 \
    --TPNSAccessInfo.0.AccessId 123 \
    --TPNSAccessInfo.0.SecretKey abc \
    --TPNSAccessInfo.0.Platform 15 \
    --TPNSAccessInfo.0.AccessKey aaa \
    --TPNSAccessInfo.0.ZoneUrl https://abc.com
```

Output: 
```
{
    "Response": {
        "TPNSUpdateRes": [
            {
                "AccessId": 123,
                "SecretKey": "abc",
                "Platform": 15,
                "AccessKey": "aaa",
                "ErrorCode": 0,
                "ErrorMessage": "ok",
                "ZoneUrl": "https://abc.com"
            }
        ],
        "RequestId": "e171fe05-990b-4f49-8111-8xb34ee957944"
    }
}
```

