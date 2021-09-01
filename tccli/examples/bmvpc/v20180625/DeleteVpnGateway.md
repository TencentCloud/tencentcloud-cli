**Example 1: 删除VPN网关**



Input: 

```
tccli bmvpc DeleteVpnGateway --cli-unfold-argument  \
    --Version 2018-06-25 \
    --VpnGatewayId bmvpngw-ab3cde
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

