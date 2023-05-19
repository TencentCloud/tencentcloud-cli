**Example 1: 获取高防ip所有规则**

获取高防ip所有规则

Input: 

```
tccli antiddos DescribeNewL7Rules --cli-unfold-argument  \
    --StatusList 1 \
    --Domain abc \
    --Business abc \
    --Ip abc \
    --Limit 1 \
    --Offset 1 \
    --ProtocolList abc \
    --Cname abc
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Region": 1,
                "Id": "abc",
                "Ip": "abc",
                "RuleId": "abc",
                "RuleName": "abc",
                "Protocol": "abc",
                "Domain": "abc",
                "LbType": 1,
                "KeepEnable": 1,
                "KeepTime": 1,
                "SourceType": 1,
                "CertType": 1,
                "SSLId": "abc",
                "Cert": "abc",
                "PrivateKey": "abc",
                "SourceList": [
                    {
                        "Source": "abc",
                        "Weight": 1,
                        "Port": 1,
                        "Backup": 1
                    }
                ],
                "Status": 1,
                "CCStatus": 1,
                "CCEnable": 1,
                "CCThreshold": 1,
                "CCLevel": "abc",
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
                "RuleId": "abc",
                "Url": "abc",
                "Interval": 1,
                "AliveNum": 1,
                "KickNum": 1,
                "Method": "abc",
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
        "RequestId": "abc"
    }
}
```

