**Example 1: DescribeVpnConnections返回示例**

查询VPN通道

Input: 

```
tccli vpc DescribeVpnConnections --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "VpnConnectionSet": [
            {
                "VpcId": "vpc-8ro3x6md",
                "VpnConnectionId": "vpnx-df9oztok",
                "VpnConnectionName": "testcon-1",
                "VpnGatewayId": "vpngw-6x0wxvtp",
                "CustomerGatewayId": "cgw-apytvc1n",
                "PreShareKey": "123",
                "VpnProto": "IPSEC",
                "EncryptProto": "IKE",
                "RouteType": "StaticRoute",
                "IKEOptionsSpecification": {
                    "PropoAuthenAlgorithm": "MD5",
                    "PropoEncryAlgorithm": "AES-CBC-128",
                    "ExchangeMode": "MAIN",
                    "LocalIdentity": "ADDRESS",
                    "RemoteIdentity": "ADDRESS",
                    "LocalAddress": "6.6.6.6",
                    "RemoteAddress": "1.1.3.2",
                    "LocalFqdnName": "",
                    "RemoteFqdnName": "",
                    "DhGroupName": "GROUP1",
                    "IKESaLifetimeSeconds": 86400,
                    "IKEVersion": "IKEV1"
                },
                "IPSECOptionsSpecification": {
                    "EncryptAlgorithm": "AES-CBC-128",
                    "IntegrityAlgorith": "MD5",
                    "PfsDhGroup": "NULL",
                    "IPSECSaLifetimeSeconds": 3600,
                    "IPSECSaLifetimeTraffic": 1843200
                },
                "CreatedTime": "2022-07-22 14:05:07",
                "SecurityPolicyDatabaseSet": [
                    {
                        "LocalCidrBlock": "0.0.0.0/0",
                        "RemoteCidrBlock": [
                            "0.0.0.0/0"
                        ]
                    }
                ],
                "State": "AVAILABLE",
                "NetStatus": "AVAILABLE",
                "NegotiationType": "flowTrigger",
                "DpdEnable": 1,
                "DpdTimeout": "30",
                "DpdAction": "clear",
                "EnableHealthCheck": false,
                "HealthCheckLocalIp": "",
                "HealthCheckRemoteIp": "",
                "HealthCheckStatus": "",
                "TagSet": []
            },
            {
                "VpcId": "vpc-8ro3x6md",
                "VpnConnectionId": "vpnx-eal8tpn2",
                "VpnConnectionName": "testcon-2",
                "VpnGatewayId": "vpngw-6x0wxvtp",
                "CustomerGatewayId": "cgw-876ql2tz",
                "PreShareKey": "123",
                "VpnProto": "IPSEC",
                "EncryptProto": "IKE",
                "RouteType": "StaticRoute",
                "IKEOptionsSpecification": {
                    "PropoAuthenAlgorithm": "MD5",
                    "PropoEncryAlgorithm": "AES-CBC-128",
                    "ExchangeMode": "MAIN",
                    "LocalIdentity": "ADDRESS",
                    "RemoteIdentity": "ADDRESS",
                    "LocalAddress": "6.6.6.6",
                    "RemoteAddress": "169.168.10.4",
                    "LocalFqdnName": "",
                    "RemoteFqdnName": "",
                    "DhGroupName": "GROUP1",
                    "IKESaLifetimeSeconds": 86400,
                    "IKEVersion": "IKEV1"
                },
                "IPSECOptionsSpecification": {
                    "EncryptAlgorithm": "AES-CBC-128",
                    "IntegrityAlgorith": "MD5",
                    "PfsDhGroup": "NULL",
                    "IPSECSaLifetimeSeconds": 3600,
                    "IPSECSaLifetimeTraffic": 1843200
                },
                "CreatedTime": "2022-07-22 14:14:48",
                "SecurityPolicyDatabaseSet": [
                    {
                        "LocalCidrBlock": "0.0.0.0/0",
                        "RemoteCidrBlock": [
                            "0.0.0.0/0"
                        ]
                    }
                ],
                "State": "AVAILABLE",
                "NetStatus": "AVAILABLE",
                "NegotiationType": "passive",
                "DpdEnable": 1,
                "DpdTimeout": "31",
                "DpdAction": "clear",
                "EnableHealthCheck": false,
                "HealthCheckLocalIp": "",
                "HealthCheckRemoteIp": "",
                "HealthCheckStatus": "",
                "TagSet": []
            }
        ],
        "RequestId": "1f4fa69d-0a9b-4342-83e1-002533feca94"
    }
}
```

