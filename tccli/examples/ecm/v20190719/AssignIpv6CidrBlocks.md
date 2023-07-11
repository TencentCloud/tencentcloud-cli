**Example 1: 申请多个运营商IPv6网段**

申请多个运营商IPv6网段


Input: 

```
tccli ecm AssignIpv6CidrBlocks --cli-unfold-argument  \
    --VpcId vpc-2loean7x \
    --ISPTypes.0.ISPType BGP \
    --ISPTypes.0.Count 1
```

Output: 
```
{
    "Response": {
        "IPv6CidrBlockSet": [
            {
                "IPv6CidrBlock": "2001::85b:3c51:f5ff:ffdb",
                "ISPType": "BGP"
            }
        ],
        "RequestId": "d4d30315-a652-47f3-a22b-598fb17a6218"
    }
}
```

