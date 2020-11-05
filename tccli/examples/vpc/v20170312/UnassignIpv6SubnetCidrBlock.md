**Example 1: Releasing the IPv6 subnet IP range**



Input: 

```
tccli vpc UnassignIpv6SubnetCidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh\
    --Ipv6SubnetCidrBlocks.0.SubnetId subnet-3s5bhzb0
```

Output: 
```
{
    "Response": {
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

