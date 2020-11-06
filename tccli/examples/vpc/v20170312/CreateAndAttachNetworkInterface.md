**Example 1: Creating an ENI and binding it to a CVM**



Input: 

```
tccli vpc CreateAndAttachNetworkInterface --cli-unfold-argument  \
    --VpcId vpc-0akbol5v \
    --SubnetId subnet-76r802pg \
    --NetworkInterfaceName TestNIC \
    --NetworkInterfaceDescription TestDesc \
    --PrivateIpAddresses.0.PrivateIpAddress 172.16.64.13 \
    --PrivateIpAddresses.0.Primary true \
    --SecondaryPrivateIpAddressCount 1 \
    --SecurityGroupIds sg-05bb4upy \
    --InstanceId ins-12345678 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
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
            "Attachment": {
                "InstanceId": "ins-12345678"
            },
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

