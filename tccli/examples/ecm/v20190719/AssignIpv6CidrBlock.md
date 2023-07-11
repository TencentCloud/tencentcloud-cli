**Example 1: 分配IPv6网段**

分配IPv6网段


Input: 

```
tccli ecm AssignIpv6CidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh \
    --ISPType CMCC
```

Output: 
```
{
    "Response": {
        "Ipv6CidrBlock": "3402:4e00:20:1000::/56",
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

