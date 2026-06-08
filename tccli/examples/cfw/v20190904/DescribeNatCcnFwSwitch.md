**Example 1: NAT配置示例**



Input: 

```
tccli cfw DescribeNatCcnFwSwitch --cli-unfold-argument  \
    --NatInsId nat-******** \
    --CcnId ccn-********
```

Output: 
```
{
    "Response": {
        "AccessInstanceList": [
            {
                "AccessCidrList": [
                    "33.224.128.0/18"
                ],
                "AccessCidrMode": 1,
                "InstanceId": "vpc-k5yzoiod",
                "InstanceRegion": "eu-frankfurt",
                "InstanceType": "VPC"
            }
        ],
        "Bypass": 0,
        "CcnId": "ccn-********",
        "RoutingMode": 1,
        "SwitchMode": 1,
        "RequestId": "7cee694a-1bfb-4deb-824e-20420654104d"
    }
}
```

