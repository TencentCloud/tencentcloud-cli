**Example 1: 创建弹性网卡并绑定云服务器**

创建弹性网卡并绑定云服务器

Input: 

```
tccli vpc CreateAndAttachNetworkInterface --cli-unfold-argument  \
    --VpcId vpc-0akbol5v \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --InstanceId ins-12345678 \
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
            "Business": "TKE",
            "CdcId": "",
            "EniType": 1,
            "AttachType": 1,
            "QosLevel": "DEFAULT",
            "ResourceId": "",
            "PrivateIpAddressSet": [
                {
                    "PrivateIpAddress": "172.16.64.13",
                    "Primary": true,
                    "AddressId": "",
                    "PublicIpAddress": "",
                    "Description": "",
                    "IsWanIpBlocked": false,
                    "State": "PENDING",
                    "QosLevel": "DEFAULT"
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

