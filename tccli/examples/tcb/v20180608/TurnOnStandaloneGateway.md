**Example 1: 开启小租户网关**



Input: 

```
tccli tcb TurnOnStandaloneGateway --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --GatewayName x-tcb-reserved-gw-envoy-demo \
    --ServiceNameList service-demo
```

Output: 
```
{
    "Response": {
        "Status": "success",
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

