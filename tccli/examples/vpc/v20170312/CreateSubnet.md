**Example 1: 创建子网**

创建子网

Input: 

```
tccli vpc CreateSubnet --cli-unfold-argument  \
    --SubnetName TestSubnet \
    --VpcId vpc-m3ul053f \
    --CidrBlock 10.8.0.0/24 \
    --Zone ap-guangzhou-1 \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "Subnet": {
            "VpcId": "vpc-m3ul053f",
            "EnableBroadcast": true,
            "Zone": "1001",
            "IsCdcSubnet": 0,
            "AvailableIpAddressCount": 1021,
            "IsRemoteVpcSnat": true,
            "SubnetName": "subnet1",
            "TotalIpAddressCount": 1024,
            "TagSet": [
                {
                    "Value": "shanghai",
                    "Key": "city"
                }
            ],
            "CreatedTime": "2023-03-21 18:00:00",
            "SubnetId": "subnet-1d32nvu2",
            "CidrBlock": "10.8.0.0/24",
            "IsDefault": false,
            "CdcId": "",
            "Ipv6CidrBlock": "",
            "RouteTableId": "",
            "NetworkAclId": ""
        },
        "RequestId": "9450a158-0487-4baa-bd3f-a07f343b6c4e"
    }
}
```

