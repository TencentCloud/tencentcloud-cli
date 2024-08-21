**Example 1: SVC更新地址**



Input: 

```
tccli vpc UpdateAddrOfSvcInternal --cli-unfold-argument  \
    --UpdateAddrOfSvcRequest.0.SvcId 123123 \
    --UpdateAddrOfSvcRequest.0.Vip 12.2.2.3 \
    --UpdateAddrOfSvcRequest.0.VirtualPort 3600 \
    --UpdateAddrOfSvcRequest.0.OldVpcId 1234567 \
    --UpdateAddrOfSvcRequest.0.OldProtocol 6 \
    --UpdateAddrOfSvcRequest.0.OldVip 12.2.2.3 \
    --UpdateAddrOfSvcRequest.0.OldVirtualPort 3700
```

Output: 
```
{
    "Response": {
        "UpdateAddrOfSvcResult": [
            {
                "SvcId": "vpce-kifyia9o",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

