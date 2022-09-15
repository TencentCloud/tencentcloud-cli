**Example 1: 设置SVC下发方式**



Input: 

```
tccli vpc ModifySvcLocationInternal --cli-unfold-argument  \
    --SetSvcLocationRequest.0.SvcId 123123 \
    --SetSvcLocationRequest.0.Client 0 \
    --SetSvcLocationRequest.0.Gateway 0 \
    --SetSvcLocationRequest.0.Rs 0
```

Output: 
```
{
    "Response": {
        "SetSvcLocationResult": [
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

