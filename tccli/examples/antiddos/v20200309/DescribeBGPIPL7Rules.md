**Example 1: 请求示例**



Input: 

```
tccli antiddos DescribeBGPIPL7Rules --cli-unfold-argument  \
    --StatusList 1 \
    --Domain www.abc.com \
    --Business bgp \
    --Ip 1.1.1.1 \
    --Limit 1 \
    --Offset 1 \
    --ProtocolList http \
    --Cname www.ab.com \
    --Export True
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Region": 1,
                "Id": "id",
                "Ip": "1.1.1.1",
                "RuleId": "id",
                "RuleName": "name",
                "Protocol": "http",
                "Domain": "www.abc.com",
                "LbType": 1,
                "KeepEnable": 1,
                "KeepTime": 1,
                "SourceType": 1,
                "CertType": 1,
                "SSLId": "id",
                "Cert": "cert",
                "PrivateKey": "key",
                "SourceList": [
                    {
                        "Source": "1.1.1.1",
                        "Weight": 1,
                        "Port": 1,
                        "Backup": 1
                    }
                ],
                "Status": 1,
                "CCStatus": 1,
                "CCEnable": 1,
                "CCThreshold": 1,
                "CCLevel": "1",
                "ModifyTime": "2020-09-22 00:00:00",
                "HttpsToHttpEnable": 1,
                "VirtualPort": 1,
                "RewriteHttps": 1,
                "ErrCode": 1,
                "Version": 1
            }
        ],
        "Healths": [
            {
                "Status": 1,
                "Enable": 1,
                "RuleId": "id",
                "Url": "url",
                "Interval": 1,
                "AliveNum": 1,
                "KickNum": 1,
                "Method": "post",
                "StatusCode": 1,
                "ProtocolFlag": 1,
                "PassiveEnable": 1,
                "BlockInter": 1,
                "FailedCountInter": 1,
                "FailedThreshold": 1,
                "PassiveStatusCode": 1,
                "PassiveStatus": 1
            }
        ],
        "Total": 1,
        "RequestId": "08afbb87-5a2c-4562-acbd-eef06a47c7db"
    }
}
```

