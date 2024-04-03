**Example 1: demo**



Input: 

```
tccli vpc DeleteAddrFromSvcInternal --cli-unfold-argument  \
    --DelAddrFromSvcRequest.0.SvcId vpce-kifyia9o \
    --DelAddrFromSvcRequest.0.Vip 12.2.2.3 \
    --DelAddrFromSvcRequest.0.VpcId 78202 \
    --DelAddrFromSvcRequest.0.Protocol 0 \
    --DelAddrFromSvcRequest.0.VirtualPort 3600
```

Output: 
```
{
    "Response": {
        "DelAddrFromSvcResult": [
            {
                "SvcId": "78202_12.2.2.3_3600_0",
                "ErrorCode": 514,
                "ErrorInfo": "Svc does't exist."
            }
        ],
        "ReturnCode": 514,
        "RequestId": "d025f464-d089-402e-afd8-12d0c9444d1c"
    }
}
```

**Example 2: SVC删除地址**



Input: 

```
tccli vpc DeleteAddrFromSvcInternal --cli-unfold-argument  \
    --DelAddrFromSvcRequest.0.SvcId 123123 \
    --DelAddrFromSvcRequest.0.Vip 12.2.2.3 \
    --DelAddrFromSvcRequest.0.VpcId 1200 \
    --DelAddrFromSvcRequest.0.Protocol 0 \
    --DelAddrFromSvcRequest.0.VirtualPort 3600
```

Output: 
```
{
    "Response": {
        "DelAddrFromSvcResult": [
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

