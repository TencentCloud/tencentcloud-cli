**Example 1: 用于获取子网内的IP地址使用详情**



Input: 

```
tccli vpc DescribeSubnetIpNumInternal --cli-unfold-argument  \
    --GetSubnetIpNumRequest.0.SubnetId 123123 \
    --GetSubnetIpNumRequest.0.Owner 123456 \
    --GetSubnetIpNumRequest.0.UniqueVpcId vpc-xxxxxxxx \
    --GetSubnetIpNumRequest.0.VpcId 12345 \
    --GetSubnetIpNumRequest.0.UniqueSubnetId subnet-xxxx
```

Output: 
```
{
    "Response": {
        "SubnetIpNumResult": [
            {
                "Subnet": "10.4.128.0",
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "Min": 168067072,
                "Max": 168099839,
                "SubnetId": 2018313,
                "Mask": "255.255.128.0",
                "Used": 4,
                "IntMask": 17,
                "UniqueSubnetId": "subnet-oiqmspv4",
                "Owner": "251197522",
                "Total": 32765,
                "AvailableNum": 32761
            },
            {
                "Subnet": "10.1.1.0",
                "VpcId": 79996,
                "UniqueVpcId": "vpc-r9u93oo3",
                "Min": 167837952,
                "Max": 167838207,
                "SubnetId": 1995599,
                "Mask": "255.255.255.0",
                "Used": 2,
                "IntMask": 24,
                "UniqueSubnetId": "subnet-9txzarp8",
                "Owner": "251197522",
                "Total": 253,
                "AvailableNum": 251
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

