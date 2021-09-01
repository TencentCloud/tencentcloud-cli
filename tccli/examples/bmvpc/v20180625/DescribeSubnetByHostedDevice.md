**Example 1: DescribeSubnetByHostedDevice**



Input: 

```
tccli bmvpc DescribeSubnetByHostedDevice --cli-unfold-argument  \
    --InstanceId chm-5im64oip \
    --Offset 2 \
    --Limit 3 \
    --Types. 7
```

Output: 
```
{
    "Response": {
        "TotalCount": 16,
        "Data": [
            {
                "VpcId": "vpc-13uonit1",
                "VpcName": "mogujie-??",
                "VpcCidrBlock": "10.50.128.0/17",
                "SubnetId": "subnet-f5lsmjdu",
                "SubnetName": "kvm-net-2183",
                "CidrBlock": "10.50.183.0/24",
                "Type": 0,
                "ZoneId": 1000400001,
                "CpmNum": 0,
                "VlanId": 2183,
                "DistributedFlag": 1,
                "DhcpEnable": 1,
                "DhcpServerIp": [
                    "10.50.183.11"
                ],
                "IpReserve": 1,
                "AvailableIpNum": 0,
                "TotalIpNum": 0,
                "SubnetCreateTime": "2017-11-20 10:34:00"
            },
            {
                "VpcId": "vpc-13uonit1",
                "VpcName": "mogujie-??",
                "VpcCidrBlock": "10.50.128.0/17",
                "SubnetId": "subnet-p7mczxs4",
                "SubnetName": "kvm-net-2184",
                "CidrBlock": "10.50.184.0/24",
                "Type": 0,
                "ZoneId": 1000400001,
                "CpmNum": 0,
                "VlanId": 2184,
                "DistributedFlag": 1,
                "DhcpEnable": 1,
                "DhcpServerIp": [
                    "10.50.184.11"
                ],
                "IpReserve": 1,
                "AvailableIpNum": 0,
                "TotalIpNum": 0,
                "SubnetCreateTime": "2017-11-20 10:39:52"
            },
            {
                "VpcId": "vpc-13uonit1",
                "VpcName": "mogujie-??",
                "VpcCidrBlock": "10.50.128.0/17",
                "SubnetId": "subnet-69x7na3y",
                "SubnetName": "kvm-net-2185",
                "CidrBlock": "10.50.185.0/24",
                "Type": 0,
                "ZoneId": 1000400001,
                "CpmNum": 0,
                "VlanId": 2185,
                "DistributedFlag": 1,
                "DhcpEnable": 1,
                "DhcpServerIp": [
                    "10.50.185.11"
                ],
                "IpReserve": 1,
                "AvailableIpNum": 0,
                "TotalIpNum": 0,
                "SubnetCreateTime": "2017-11-20 10:39:53"
            }
        ],
        "RequestId": "25465fbf-df82-417e-9d75-040e7b76f479"
    }
}
```

