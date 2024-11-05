**Example 1: 查询SIP通道列表示例**

查询SIP通道列表示例

Input: 

```
tccli ccc DescribeSipTrunkList --cli-unfold-argument  \
    --Filters.0.Name FuzzingKeyWord \
    --Filters.0.Values  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "a7c5df8c-a960-47f3-afe5-5284bcb5591d",
        "TotalCount": 1,
        "SipTrunkList": [
            {
                "Id": 2158,
                "Name": "11",
                "Uin": "10003910000",
                "AppId": 133050000,
                "Mode": "REGISTER",
                "CheckHealth": false,
                "ProviderId": 200,
                "AllowIpList": [],
                "WhiteIpList": [],
                "RegisterUserName": "gateway10003910000",
                "RegisterPassword": "xxxxxxxx",
                "RegisterServer": "sip.tccc.qcloud.com",
                "RegisterServerPort": 35090,
                "RegisterServerTCPPort": 35090,
                "RegisterServerTLSPort": 5061,
                "RegisterOutboundProxy": "sip.tccc.qcloud.com",
                "RegisterOutboundProxyBak": "sip2.tccc.qcloud.com",
                "RegisterOutboundProxyPort": 0,
                "RegisterOutboundProxyTCPPort": 35090,
                "RegisterOutboundProxyTLSPort": 5061,
                "RegisterProto": "UDP",
                "RegisterFullName": "gatewayxxxxxxxx@sip.tccc.qcloud.com",
                "RegisterExpires": 3600,
                "InboundCalleeFormat": "NUMBER",
                "InboundCalleeField": "TO",
                "OutboundCallerFormat": "NUMBER",
                "OutboundCalleeFormat": "",
                "State": 1,
                "RegisterStatus": "NOT_REGISTERED_STATE",
                "HealthStatus": ""
            }
        ]
    }
}
```

