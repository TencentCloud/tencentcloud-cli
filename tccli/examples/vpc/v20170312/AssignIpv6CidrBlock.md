**Example 1: Assigning an IPv6 IP range**



Input: 

```
tccli vpc AssignIpv6CidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh
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

