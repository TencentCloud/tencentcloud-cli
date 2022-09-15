**Example 1: SVC新增地址**



Input: 

```
tccli vpc CreateAddrToSvcInternal --cli-unfold-argument  \
    --AddAddrToSvcRequest.0.SvcId 123123 \
    --AddAddrToSvcRequest.0.Vip 12.2.2.3 \
    --AddAddrToSvcRequest.0.VpcId 1200 \
    --AddAddrToSvcRequest.0.Protocol 0 \
    --AddAddrToSvcRequest.0.VirtualPort 3600
```

Output: 
```
{
    "Response": {
        "AddAddrToSvcResult": [
            {
                "SvcId": "78202_12.2.2.3_3600_0",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

