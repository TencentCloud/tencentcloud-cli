**Example 1: 创建VPN通道**

创建VPN通道

Input: 

```
tccli vpc CreateVpnConnection --cli-unfold-argument  \
    --VpnConnectionName TEST_CONN \
    --PreShareKey 654321 \
    --VpcId vpc-gapcv96p \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --IPSECOptionsSpecification.PfsDhGroup NULL \
    --IPSECOptionsSpecification.EncryptAlgorithm 3DES-CBC \
    --IPSECOptionsSpecification.IntegrityAlgorith MD5 \
    --SecurityPolicyDatabases.0.LocalCidrBlock 10.8.4.0/24 \
    --SecurityPolicyDatabases.0.RemoteCidrBlock 58.211.1.0/24 \
    --VpnGatewayId vpngw-1w9tue3d \
    --CustomerGatewayId cgw-qa9sxpy7 \
    --IKEOptionsSpecification.IKEVersion IKEV1 \
    --IKEOptionsSpecification.RemoteIdentity ADDRESS \
    --IKEOptionsSpecification.PropoAuthenAlgorithm MD5 \
    --IKEOptionsSpecification.RemoteAddress 1.2.3.4 \
    --IKEOptionsSpecification.LocalIdentity ADDRESS \
    --IKEOptionsSpecification.LocalAddress 58.211.2.5 \
    --IKEOptionsSpecification.ExchangeMode MAIN \
    --IKEOptionsSpecification.PropoEncryAlgorithm 3DES-CBC \
    --IKEOptionsSpecification.DhGroupName GROUP1
```

Output: 
```
{
    "Response": {
        "VpnConnection": {
            "VpcId": "vpc-kozprpc9",
            "VpnConnectionId": "vpnx-p0j11j28",
            "VpnConnectionName": "test-con",
            "VpnGatewayId": "vpngw-ecvft20x",
            "CustomerGatewayId": "cgw-7lhl5331",
            "State": "PENDING",
            "PreShareKey": "123456",
            "NegotiationType": "",
            "DpdEnable": -1,
            "DpdTimeout": "",
            "DpdAction": "",
            "VpnProto": "IPSEC",
            "EncryptProto": "IKE",
            "RouteType": "STATIC",
            "CreatedTime": "0000-00-00 00:00:00",
            "NetStatus": "",
            "SecurityPolicyDatabaseSet": [],
            "IKEOptionsSpecification": {
                "PropoEncryAlgorithm": "AES-CBC-256",
                "PropoAuthenAlgorithm": "SHA",
                "ExchangeMode": "AGGRESSIVE",
                "LocalIdentity": "ADDRESS",
                "RemoteIdentity": "ADDRESS",
                "LocalAddress": "122.152.199.99",
                "RemoteAddress": "39.97.38.104",
                "LocalFqdnName": "",
                "RemoteFqdnName": "",
                "DhGroupName": "GROUP2",
                "IKESaLifetimeSeconds": 86400,
                "IKEVersion": "IKEV1"
            },
            "IPSECOptionsSpecification": {
                "EncryptAlgorithm": "AES-CBC-256",
                "IntegrityAlgorith": "SHA1",
                "IPSECSaLifetimeSeconds": 3600,
                "IPSECSaLifetimeTraffic": 1843200,
                "PfsDhGroup": "NULL"
            },
            "EnableHealthCheck": false,
            "HealthCheckLocalIp": "",
            "HealthCheckRemoteIp": "",
            "HealthCheckStatus": "",
            "TagSet": []
        },
        "RequestId": "4b71dd4d-a3ee-4ac1-b99a-99d65f6443fd"
    }
}
```

