**Example 1: 修改WAF的高防EIP**



Input: 

```
tccli waf ModifyWafAntiDDoSEip --cli-unfold-argument  \
    --OperateType 2 \
    --InstanceId waf_2kzdlcpm00gmf6bv \
    --EipId eip-di8soa5d \
    --Eip 222.22.2.2 \
    --EipRegion ap-guangzhou \
    --InnerIp 30.166.111.32
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

