**Example 1: 修改对端网关**

修改对端网关

Input: 

```
tccli vpc ModifyCustomerGatewayAttribute --cli-unfold-argument  \
    --CustomerGatewayId cgw-mgp33pll \
    --CustomerGatewayName NewName
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

