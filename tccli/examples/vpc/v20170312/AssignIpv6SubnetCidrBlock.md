**Example 1: Assigning an IPv6 subnet IP range**



Input: 

```
tccli vpc AssignIpv6SubnetCidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh\
    --Ipv6SubnetCidrBlocks.0.SubnetId subnet-3s5bhzb0\
    --Ipv6SubnetCidrBlocks.0.Ipv6CidrBlock 3402:4e00:20:1202::/64
```

Output: 
```
{
    "Response": {
        "Ipv6SubnetCidrBlockSet": [
            {
                "SubnetId": "subnet-ewhv1m9e",
                "Ipv6CidrBlock": "3402:4e00:20:1201::/64"
            },
            {
                "SubnetId": "subnet-3s5bhzb0",
                "Ipv6CidrBlock": "3402:4e00:20:1202::/64"
            }
        ],
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

