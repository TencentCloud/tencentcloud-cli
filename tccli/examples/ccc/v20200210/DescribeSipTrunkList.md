**Example 1: 查询SIP通道列表示例**



Input: 

```
tccli ccc DescribeSipTrunkList --cli-unfold-argument  \
    --Filters.0.Name Mode \
    --Filters.0.Values REGISTER \
    --All True
```

Output: 
```
{
    "Response": {
        "SipTrunkList": [
            {
                "AllowIpList": [],
                "AppId": 251202066,
                "CheckHealth": false,
                "DownloadVolume": 0,
                "HealthStatus": "",
                "Id": 15063,
                "InboundCalleeField": "TO",
                "InboundCalleeFormat": "NUMBER",
                "Mode": "REGISTER",
                "Name": "jackson",
                "OutboundCalleeFormat": "",
                "OutboundCallerFormat": "NUMBER",
                "OutboundCodecList": [],
                "OutboundForceFixNAT": false,
                "ProviderId": 255,
                "RegisterExpires": 3600,
                "RegisterFullName": "gateway70000016028615063@sip-dev.tccc.qcloud.com",
                "RegisterOutboundProxy": "sip-dev.tccc.qcloud.com",
                "RegisterOutboundProxyBak": "sip2-dev.tccc.qcloud.com",
                "RegisterOutboundProxyPort": 0,
                "RegisterOutboundProxyTCPPort": 35090,
                "RegisterOutboundProxyTLSPort": 5061,
                "RegisterPassword": "6C8JaZEQyoR0",
                "RegisterProto": "UDP",
                "RegisterServer": "sip-dev.tccc.qcloud.com",
                "RegisterServerPort": 35090,
                "RegisterServerTCPPort": 35090,
                "RegisterServerTLSPort": 5061,
                "RegisterStatus": "NOT_REGISTERED_STATE",
                "RegisterUserName": "gateway70000016028615063",
                "State": 1,
                "Uin": "700000160286",
                "UploadVolume": 0,
                "WhiteIpList": []
            }
        ],
        "TotalCount": 416,
        "RequestId": "675b4a1f-75bc-4198-8abc-9501b43926f7"
    }
}
```

