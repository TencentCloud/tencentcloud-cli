**Example 1: 查询域名列表**

接入标签鉴权。

Input: 

```
tccli live DescribeLiveDomains --cli-unfold-argument  \
    --IsDelayLive 0 \
    --PageSize 10 \
    --PageNum 1 \
    --DomainStatus 1 \
    --DomainType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "AllCount": 2,
        "CreateLimitCount": 0,
        "PlayTypeCount": [
            1,
            2,
            3
        ],
        "DomainList": [
            {
                "Name": "abc.com",
                "IsMiniProgramLive": 0,
                "Type": 1,
                "Status": 1,
                "PlayType": 1,
                "IsDelayLive": 0,
                "CreateTime": "2018-08-29 10:00:00",
                "BCName": 1,
                "CurrentCName": "",
                "TargetDomain": "abc.com.liveplay.myqcloud.com",
                "RentTag": 0,
                "RentExpireTime": "0000-00-00 00:00:00"
            }
        ]
    }
}
```

