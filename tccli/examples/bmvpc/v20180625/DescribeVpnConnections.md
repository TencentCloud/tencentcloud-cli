**Example 1: 查询VPN通道列表**



Input: 

```
tccli bmvpc DescribeVpnConnections --cli-unfold-argument  \
    --Version 2018-06-25
```

Output: 
```
{
    "Response": {
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b",
        "TotalCount": 1,
        "VpnConnectionSet": [
            {
                "VpcId": "vpc-0a36uwkr",
                "VpnConnectionId": "vpnx-5p7vkch8",
                "VpnConnectionName": "testjoan",
                "VpnGatewayId": "vpngw-p4lmqawn",
                "CustomerGatewayId": "cgw-l4rblw63",
                "PreShareKey": "123456",
                "VpnProto": "IPSEC",
                "IKEOptionsSpecification": {
                    "PropoAuthenAlgorithm": "MD5",
                    "PropoEncryAlgorithm": "3DES-CBC",
                    "ExchangeMode": "MAIN",
                    "LocalIdentity": "ADDRESS",
                    "RemoteIdentity": "ADDRESS",
                    "LocalAddress": "183.60.249.17",
                    "RemoteAddress": "183.60.249.126",
                    "LocalFqdnName": "",
                    "RemoteFqdnName": "",
                    "DhGroupName": "GROUP1",
                    "IKESaLifetimeSeconds": "86400",
                    "IKEVersion": "IKEV1"
                },
                "IPSECOptionsSpecification": {
                    "EncryptAlgorithm": "3DES-CBC",
                    "IntegrityAlgorith": "MD5",
                    "EncapMode": "TUNNEL",
                    "SecurityProto": "ESP",
                    "PfsDhGroup": "NULL",
                    "IPSECSaLifetimeSeconds": "3600",
                    "IPSECSaLifetimeTraffic": "1843200"
                },
                "CreateTime": "2017-08-0510: 27: 32",
                "State": "AVAILABLE",
                "NetStatus": "UNAVAILABLE",
                "SecurityPolicyDatabaseSet": [
                    {
                        "LocalCidrBlock": "172.16.0.0/16",
                        "RemoteCidrBlock": [
                            "10.10.0.0/16"
                        ]
                    }
                ]
            }
        ]
    }
}
```

