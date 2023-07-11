**Example 1: 分配IPv6子网段**

申请IPv6子网


Input: 

```
tccli ecm AssignIpv6SubnetCidrBlock --cli-unfold-argument  \
    --VpcId vpc-q26u781x \
    --Ipv6SubnetCidrBlocks.0.SubnetId subnet-8uwg949c \
    --Ipv6SubnetCidrBlocks.0.Ipv6CidrBlock 2001::85b:3c51:f5ff:ffdb
```

Output: 
```
{
    "Response": {
        "Ipv6SubnetCidrBlockSet": [
            {
                "SubnetId": "subnet-8uwg949c",
                "Ipv6CidrBlock": "2001::85b:3c51:f5ff:ffdb"
            }
        ],
        "RequestId": "d681727c-6291-4409-9ab6-6ecbb493243c"
    }
}
```

