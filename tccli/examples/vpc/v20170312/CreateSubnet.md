**Example 1: 创建子网**



Input: 

```
tccli vpc CreateSubnet --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-m3ul053f\
    --SubnetName TestSubnet\
    --CidrBlock 10.8.0.0/16\
    --Zone ap-guangzhou-1\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Subnet": {
            "VpcId": "vpc-m3ul053f",
            "IsDefault": false,
            "SubnetName": "TestSubnet",
            "Zone": "ap-guangzhou-1",
            "SubnetId": "subnet-2qhl25io",
            "CidrBlock": "10.8.255.0/24",
            "TotalIpAddressCount": 253,
            "AvailableIpAddressCount": 253,
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        }
    }
}
```

