**Example 1: 创建VPN通道**

创建VPN通道

Input: 

```
tccli vpc CreateVpnConnection --cli-unfold-argument  \
    --VpnConnectionName TEST_CONN \
    --PreShareKey 6325ac \
    --VpcId vpc-gapcv96p \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --IPSECOptionsSpecification.PfsDhGroup NULL \
    --IPSECOptionsSpecification.EncryptAlgorithm 3DES-CBC \
    --IPSECOptionsSpecification.IntegrityAlgorith SHA1 \
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
            "VpcId": "vpc-gapcv96p",
            "VpnConnectionId": "vpnx-axc13cega",
            "VpnConnectionName": "TEST_CONN",
            "VpnGatewayId": "vpngw-1w9tue3d",
            "CustomerGatewayId": "cgw-qa9sxpy7",
            "State": "PENDING",
            "PreShareKey": "6325ac",
            "NegotiationType": "active",
            "DpdEnable": -1,
            "DpdTimeout": "30",
            "DpdAction": "clear",
            "VpnProto": "IPSEC",
            "EncryptProto": "IKE",
            "RouteType": "STATIC",
            "CreatedTime": "0000-00-00 00:00:00",
            "NetStatus": "AVAILABLE",
            "SecurityPolicyDatabaseSet": [],
            "IKEOptionsSpecification": {
                "PropoEncryAlgorithm": "3DES-CBC",
                "PropoAuthenAlgorithm": "MD5",
                "ExchangeMode": "MAIN",
                "LocalIdentity": "ADDRESS",
                "RemoteIdentity": "ADDRESS",
                "LocalAddress": "58.211.2.5",
                "RemoteAddress": "1.2.3.4",
                "LocalFqdnName": "local-name",
                "RemoteFqdnName": "remote-name",
                "DhGroupName": "GROUP1",
                "IKESaLifetimeSeconds": 86400,
                "IKEVersion": "IKEV1"
            },
            "IPSECOptionsSpecification": {
                "EncryptAlgorithm": "3DES-CBC",
                "IntegrityAlgorith": "SHA1",
                "IPSECSaLifetimeSeconds": 3600,
                "IPSECSaLifetimeTraffic": 1843200,
                "PfsDhGroup": "NULL"
            },
            "EnableHealthCheck": false,
            "HealthCheckLocalIp": "169.254.168.2",
            "HealthCheckRemoteIp": "169.254.168.1",
            "HealthCheckStatus": "AVAILABLE",
            "TagSet": []
        },
        "RequestId": "4b71dd4d-a3ee-4ac1-b99a-99d65f6443fd"
    }
}
```

