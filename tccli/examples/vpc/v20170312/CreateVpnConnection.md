**Example 1: 创VPN通道**



Input: 

```
tccli vpc CreateVpnConnection --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-gapcv96p\
    --VpnGatewayId vpngw-1w9tue3d\
    --CustomerGatewayId cgw-qa9sxpy7\
    --VpnConnectionName TEST_CONN\
    --PreShareKey 654321\
    --SecurityPolicyDatabases.0.LocalCidrBlock 10.8.4.0/24\
    --SecurityPolicyDatabases.0.RemoteCidrBlock 58.211.1.0/24\
    --IKEOptionsSpecification.DhGroupName GROUP1\
    --IKEOptionsSpecification.ExchangeMode MAIN\
    --IKEOptionsSpecification.IKEVersion IKEV1\
    --IKEOptionsSpecification.LocalAddress 58.211.2.5\
    --IKEOptionsSpecification.LocalIdentity ADDRESS\
    --IKEOptionsSpecification.PropoAuthenAlgorithm MD5\
    --IKEOptionsSpecification.PropoEncryAlgorithm 3DES-CBC\
    --IKEOptionsSpecification.RemoteAddress 1.2.3.4\
    --IKEOptionsSpecification.RemoteIdentity ADDRESS\
    --IPSECOptionsSpecification.EncryptAlgorithm 3DES-CBC\
    --IPSECOptionsSpecification.IntegrityAlgorith MD5\
    --IPSECOptionsSpecification.PfsDhGroup NULL\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "VpnConnection": {
            "VpcId": "vpc-gapcv96p",
            "VpnConnectionName": "TEST_CONN",
            "VpnGatewayId": "vpngw-1w9tue3d",
            "CustomerGatewayId": "cgw-qa9sxpy7",
            "State": "PENDING"
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

