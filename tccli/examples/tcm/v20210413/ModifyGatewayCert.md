**Example 1: 修改 Gateway 证书**



Input: 

```
tccli tcm ModifyGatewayCert --cli-unfold-argument  \
    --MeshID abc \
    --GatewayName abc \
    --GatewayNamespace abc \
    --PortName abc \
    --NewCertID abc \
    --OldCertID abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

