**Example 1: 修改对端网关**



Input: 

```
tccli bmvpc ModifyCustomerGatewayAttribute --cli-unfold-argument  \
    --Version 2018-06-25 \
    --CustomerGatewayId bmcgw-mgp33pll \
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

