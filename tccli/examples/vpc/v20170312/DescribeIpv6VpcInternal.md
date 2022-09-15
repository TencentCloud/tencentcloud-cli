**Example 1: demo**



Input: 

```
tccli vpc DescribeIpv6VpcInternal --cli-unfold-argument  \
    --Owner 251197522
```

Output: 
```
{
    "Response": {
        "GetIPv6VpcResult": [
            {
                "VpcId": 79996,
                "UniqueVpcId": "vpc-r9u93oo3",
                "IntPrefix": 56,
                "ZoneId": 100002,
                "Flag": 1,
                "Address": "2402:4e00:1001:2f00::",
                "Owner": "251197522",
                "Type": 0,
                "CreateTime": "0000-00-00 00:00:00"
            },
            {
                "VpcId": 78202,
                "UniqueVpcId": "vpc-g6z0p6bv",
                "IntPrefix": 56,
                "ZoneId": 100002,
                "Flag": 1,
                "Address": "2402:4e00:1001:3200::",
                "Owner": "251197522",
                "Type": 0,
                "CreateTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "3ae6fef5-2654-4a9a-8e07-0346133087e9"
    }
}
```

