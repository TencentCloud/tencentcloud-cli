**Example 1: 创建弹性网卡**



Input: 

```
tccli vpc CreateNetworkInterface --cli-unfold-argument  \
    --VpcId vpc-0akbol5v \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --PrivateIpAddresses.0.Primary true \
    --PrivateIpAddresses.0.PrivateIpAddress 172.16.64.13 \
    --SecurityGroupIds sg-05bb4upy \
    --NetworkInterfaceDescription TestDesc \
    --SecondaryPrivateIpAddressCount 1 \
    --SubnetId subnet-76r802pg \
    --NetworkInterfaceName TestNIC
```

Output: 
```
{
    "Response": {
        "NetworkInterface": {
            "NetworkInterfaceId": "eni-irk5qhhl",
            "VpcId": "vpc-0akbol5v",
            "SubnetId": "subnet-76r802pg",
            "NetworkInterfaceName": "TestNIC",
            "NetworkInterfaceDescription": "TestDesc",
            "MacAddress": "20:90:6F:62:33:E2",
            "Business": "xx",
            "CdcId": "xx",
            "EniType": 1,
            "AttachType": 1,
            "PrivateIpAddressSet": [
                {
                    "PrivateIpAddress": "172.16.64.13",
                    "Primary": true,
                    "AddressId": "",
                    "PublicIpAddress": "",
                    "Description": "",
                    "IsWanIpBlocked": false,
                    "State": "PENDING"
                }
            ],
            "Attachment": null,
            "GroupSet": [],
            "Primary": false,
            "State": "PENDING",
            "Zone": "",
            "CreatedTime": "",
            "Ipv6AddressSet": [],
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ]
        },
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

