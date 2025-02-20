**Example 1: 获取高防ip所有规则**

获取高防ip所有规则

Input: 

```
tccli antiddos DescribeNewL7Rules --cli-unfold-argument  \
    --StatusList 1 \
    --Domain www.abc.com \
    --Business bgp \
    --Ip 1.1.1.1 \
    --Limit 1 \
    --Offset 1 \
    --ProtocolList 1.1.1.1 \
    --Cname www.abc.com
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Region": 1,
                "Id": "bgp-121",
                "Ip": "1.1.1.1",
                "RuleId": "idxxx",
                "RuleName": "namexxx",
                "Protocol": "http",
                "Domain": "www.abc.com",
                "LbType": 1,
                "KeepEnable": 1,
                "KeepTime": 1,
                "SourceType": 1,
                "CertType": 1,
                "SSLId": "idxxx",
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
                "CCLevel": "2",
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
                "RuleId": "ruleid",
                "Url": "url",
                "Interval": 1,
                "AliveNum": 1,
                "KickNum": 1,
                "Method": "get",
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

