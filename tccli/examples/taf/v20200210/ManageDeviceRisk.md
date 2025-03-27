**Example 1: 查询oaid_md5评分**



Input: 

```
tccli taf ManageDeviceRisk --cli-unfold-argument  \
    --BusinessSecurityData.OsType 1 \
    --BusinessSecurityData.DeviceType 6 \
    --BusinessSecurityData.DeviceId 6c31deb89af12f3bc1aa1e694f919820 \
    --BusinessSecurityData.ClientIp 81.177.207.88
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "Score": 100
            }
        },
        "RequestId": "a56981e9-00b2-4bd1-889e-e3733fd4be35"
    }
}
```

