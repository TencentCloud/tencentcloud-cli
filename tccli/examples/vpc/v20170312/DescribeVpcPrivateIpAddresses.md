**Example 1: 批量查询VPC内网IP信息**

批量查询VPC内网IP信息

Input: 

```
tccli vpc DescribeVpcPrivateIpAddresses --cli-unfold-argument  \
    --VpcId vpc-rkxd3pgh \
    --PrivateIpAddresses 10.4.2.2 10.4.2.3 10.4.2.17
```

Output: 
```
{
    "Response": {
        "VpcPrivateIpAddressSet": [
            {
                "PrivateIpAddress": "10.4.2.2",
                "PrivateIpAddressType": "CTSDB",
                "CidrBlock": "10.4.2.0/24",
                "CreatedTime": "2018-12-27 15:40:10"
            },
            {
                "PrivateIpAddress": "10.4.2.3",
                "PrivateIpAddressType": "CFS",
                "CidrBlock": "10.4.2.0/24",
                "CreatedTime": "2018-09-02 16:48:59"
            },
            {
                "PrivateIpAddress": "10.4.2.17",
                "PrivateIpAddressType": "CVM",
                "CidrBlock": "10.4.2.0/24",
                "CreatedTime": "2018-09-02 16:48:59"
            }
        ],
        "RequestId": "75221557-b667-440a-8cfe-ccd1bde2a234"
    }
}
```

