**Example 1: 创建弹性网卡**

创建弹性网卡

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
            "NetworkInterfaceId": "abc",
            "NetworkInterfaceName": "abc",
            "NetworkInterfaceDescription": "abc",
            "SubnetId": "abc",
            "VpcId": "abc",
            "GroupSet": [
                "abc"
            ],
            "Primary": true,
            "MacAddress": "abc",
            "State": "abc",
            "PrivateIpAddressSet": [
                {
                    "PrivateIpAddress": "abc",
                    "Primary": true,
                    "PublicIpAddress": "abc",
                    "AddressId": "abc",
                    "Description": "abc",
                    "IsWanIpBlocked": true,
                    "State": "abc",
                    "QosLevel": "abc"
                }
            ],
            "Attachment": {
                "InstanceId": "abc",
                "DeviceIndex": 1,
                "InstanceAccountId": "abc",
                "AttachTime": "abc"
            },
            "Zone": "abc",
            "CreatedTime": "abc",
            "Ipv6AddressSet": [
                {
                    "Address": "abc",
                    "Primary": true,
                    "AddressId": "abc",
                    "Description": "abc",
                    "IsWanIpBlocked": true,
                    "State": "abc"
                }
            ],
            "TagSet": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "EniType": 1,
            "Business": "abc",
            "CdcId": "abc",
            "AttachType": 1,
            "ResourceId": "abc",
            "QosLevel": "abc"
        },
        "RequestId": "abc"
    }
}
```

