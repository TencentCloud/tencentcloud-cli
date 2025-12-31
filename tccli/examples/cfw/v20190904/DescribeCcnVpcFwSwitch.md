**Example 1: 获取防火墙配置**



Input: 

```
tccli cfw DescribeCcnVpcFwSwitch --cli-unfold-argument  \
    --CcnId ccn-c0qmm031
```

Output: 
```
{
    "Response": {
        "InterconnectPairs": [
            {
                "GroupA": [
                    {
                        "AccessCidrList": [
                            "33.224.32.0/20"
                        ],
                        "AccessCidrMode": 1,
                        "InstanceId": "vpc-k5yzoiod",
                        "InstanceRegion": "eu-frankfurt",
                        "InstanceType": "VPC"
                    }
                ],
                "GroupB": [
                    {
                        "AccessCidrList": [
                            "10.70.0.0/22"
                        ],
                        "AccessCidrMode": 1,
                        "InstanceId": "vpc-lvxgi7fi",
                        "InstanceRegion": "ap-hongkong",
                        "InstanceType": "VPC"
                    }
                ],
                "InterconnectMode": "CrossConnect"
            }
        ],
        "RequestId": "dff5ad62-9f79-44a3-ba36-3b66d85e739a"
    }
}
```

