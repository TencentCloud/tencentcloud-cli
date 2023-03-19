**Example 1: 查询SIP通道列表示例**

查询SIP通道列表示例

Input: 

```
tccli ccc DescribeSipTrunkList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name xx \
    --Filters.0.Values xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SipTrunkList": [
            {
                "Id": 0,
                "Uin": "abc",
                "AppId": 1,
                "Mode": "abc",
                "CheckHealth": true,
                "ProviderId": 0,
                "RegisterUserName": "abc",
                "RegisterPassword": "abc",
                "RegisterServer": "abc",
                "RegisterServerPort": 0,
                "RegisterOutboundProxy": "abc",
                "RegisterOutboundProxyPort": 0,
                "RegisterProto": "abc",
                "RegisterFullName": "abc",
                "RegisterExpires": 0,
                "InboundCalleeFormat": "abc",
                "InboundCalleeField": "abc",
                "OutboundCallerFormat": "abc",
                "State": 0,
                "AllowIpList": [
                    {
                        "Host": "abc",
                        "Port": 0
                    }
                ],
                "RegisterStatus": "abc",
                "HealthStatus": "abc",
                "Name": "abc",
                "RegisterServerTCPPort": 0,
                "RegisterServerTLSPort": 0,
                "RegisterOutboundProxyTCPPort": 0,
                "RegisterOutboundProxyTLSPort": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

