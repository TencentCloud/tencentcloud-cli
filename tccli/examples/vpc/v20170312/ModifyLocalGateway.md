**Example 1: 修改本地网关**

修改本地网关

Input: 

```
tccli vpc ModifyLocalGateway --cli-unfold-argument  \
    --LocalGatewayName test1 \
    --CdcId cluster-1234dert \
    --LocalGatewayId lgw-1234edfr
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

