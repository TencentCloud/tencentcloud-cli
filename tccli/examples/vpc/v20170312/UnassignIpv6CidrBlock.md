**Example 1: 释放IPv6网段**

释放IPv6网段

Input: 

```
tccli vpc UnassignIpv6CidrBlock --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh \
    --Ipv6CidrBlock 3402:4e00:20:1000::/56
```

Output: 
```
{
    "Response": {
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

