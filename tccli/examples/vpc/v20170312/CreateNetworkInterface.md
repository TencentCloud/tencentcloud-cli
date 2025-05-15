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
    --NetworkInterfaceDescription demo \
    --SecondaryPrivateIpAddressCount 1 \
    --SubnetId subnet-76r802pg \
    --NetworkInterfaceName demo
```

Output: 
```
{
    "Response": {
        "NetworkInterface": {
            "AttachType": 0,
            "Attachment": null,
            "Business": "cvm",
            "CdcId": "",
            "CreatedTime": "",
            "EniType": 0,
            "GroupSet": [],
            "Ipv6AddressSet": [],
            "MacAddress": "20:90:6F:2A:11:3D",
            "NetworkInterfaceDescription": "",
            "NetworkInterfaceId": "eni-ndaunxuo",
            "NetworkInterfaceName": "demo",
            "Primary": false,
            "PrivateIpAddressSet": [
                {
                    "AddressId": "",
                    "Description": "",
                    "IsWanIpBlocked": false,
                    "Primary": true,
                    "PrivateIpAddress": "10.0.0.3",
                    "PublicIpAddress": "",
                    "QosLevel": "PT",
                    "State": "PENDING"
                }
            ],
            "QosLevel": "PT",
            "ResourceId": "",
            "State": "PENDING",
            "SubnetId": "subnet-r8x0gown",
            "TagSet": [],
            "VpcId": "vpc-67kr6ava",
            "Zone": ""
        },
        "RequestId": "a5c5cd4d-9024-4465-a8c0-5b0979ec806e"
    }
}
```

