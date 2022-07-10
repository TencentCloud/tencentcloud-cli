**Example 1: 获取7层规则**



Input: 

```
tccli antiddos DescribeNewL7Rules --cli-unfold-argument  \
    --StatusList 1 \
    --Domain xx \
    --Business xx \
    --Ip xx \
    --Limit 1 \
    --Offset 1 \
    --ProtocolList xx
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "KeepTime": 1,
                "HttpsToHttpEnable": 1,
                "Status": 1,
                "LbType": 1,
                "CCLevel": "xx",
                "CCEnable": 1,
                "CCThreshold": 1,
                "Region": 1,
                "VirtualPort": 1,
                "SourceList": [
                    {
                        "Source": "xx",
                        "Weight": 1
                    },
                    {
                        "Source": "xx",
                        "Weight": 1
                    }
                ],
                "Cert": "xx",
                "KeepEnable": 1,
                "ModifyTime": "2020-09-22 00:00:00",
                "Domain": "xx",
                "Protocol": "xx",
                "SourceType": 1,
                "RuleId": "xx",
                "Ip": "xx",
                "PrivateKey": "xx",
                "CertType": 1,
                "RuleName": "xx",
                "CCStatus": 1,
                "SSLId": "xx",
                "Id": "xx"
            }
        ],
        "Healths": [
            {
                "Status": 1,
                "Enable": 1,
                "RuleId": "xx",
                "Url": "xx",
                "Interval": 1,
                "AliveNum": 1,
                "KickNum": 1,
                "Method": "xx",
                "StatusCode": 1
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

