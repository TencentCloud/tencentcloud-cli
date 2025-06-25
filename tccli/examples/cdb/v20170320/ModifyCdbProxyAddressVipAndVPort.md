**Example 1: 修改数据库代理地址VPC**



Input: 

```
tccli cdb ModifyCdbProxyAddressVipAndVPort --cli-unfold-argument  \
    --ProxyGroupId proxy-il2nlsdn \
    --ProxyAddressId proxyaddr-mc0efsw0 \
    --UniqVpcId vpc-ixw3ll2d \
    --UniqSubnetId subnet-0z3r56vq
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

