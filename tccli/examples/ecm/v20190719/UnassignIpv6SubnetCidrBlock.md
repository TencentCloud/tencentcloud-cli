**Example 1: 释放IPv6子网段**

释放IPv6子网段


Input: 

```
tccli ecm UnassignIpv6SubnetCidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh \
    --Ipv6SubnetCidrBlocks.0.SubnetId subnet-ewhv1m9e \
    --Ipv6SubnetCidrBlocks.1.SubnetId subnet-3s5bhzb0
```

Output: 
```
{
    "Response": {
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

