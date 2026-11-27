**Example 1: 按防护实例 ID 查询防护策略**

查询防护实例 `prot-3t4pafh3u10f` 的 DDoS 防护策略详情。

Input: 

```
tccli antiddos DescribeDDoSProtectionPolicy --cli-unfold-argument  \
    --ProtectionId prot-3t4pafh3u10f
```

Output: 
```
{
    "Response": {
        "ProtectionPolicy": {
            "DefaultProtection": {
                "SensitivityLevel": "high"
            },
            "IPACLRules": {
                "Rules": [
                    {
                        "Action": "drop",
                        "IPs": [
                            "1.1.1.1"
                        ]
                    }
                ]
            },
            "GeoBlocking": {
                "GeoCode": [
                    "AF"
                ]
            },
            "ProtocolBlocking": {
                "TCPProtocol": "on",
                "UDPProtocol": "off",
                "ICMPProtocol": "on",
                "OtherProtocol": "off"
            },
            "ConnectionProtection": {
                "SourceIPNewConnectionLimit": 111,
                "AbnormalConnectionLimit": {
                    "AbnormalConnectThreshold": 4,
                    "AbnormalConnectCondition": {
                        "EmptyConnection": "off"
                    }
                }
            }
        },
        "RequestId": "5eb8d33a-dc1a-4cdf-9ccf-7ace3ee15d46"
    }
}
```

