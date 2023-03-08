**Example 1: 查询SIP通道列表示例**

查询SIP通道列表示例

Input: 

```
tccli ccc DescribeSipTrunkList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SipTrunkList": [
            {
                "Id": 0,
                "Uin": "xx",
                "AppId": "xx",
                "Mode": "xx",
                "CheckHealth": true,
                "ProviderId": 0,
                "RegisterUserName": "xx",
                "RegisterPassword": "xx",
                "RegisterServer": "xx",
                "RegisterServerPort": 0,
                "RegisterOutboundProxy": "xx",
                "RegisterOutboundProxyPort": 0,
                "RegisterProto": "xx",
                "RegisterFullName": "xx",
                "RegisterExpires": 0,
                "InboundCalleeFormat": "xx",
                "InboundCalleeField": "xx",
                "OutboundCallerFormat": "xx",
                "State": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

