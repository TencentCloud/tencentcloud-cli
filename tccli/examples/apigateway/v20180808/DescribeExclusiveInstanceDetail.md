**Example 1: DescribeExclusiveInstanceDetail**



Input: 

```
tccli apigateway DescribeExclusiveInstanceDetail --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceId": "instance-0c96l2bo",
            "Zone": "ap-guangzhou-1",
            "Zones": [
                "ap-guangzhou-1"
            ],
            "InstanceName": "test_instance",
            "InstanceDescription": "",
            "InstanceChargeType": "PREPAID",
            "InstanceState": "RUNNING",
            "InstanceChargePrepaid": {
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "ExpiredTime": "2018-10-30T04:24:19"
            },
            "InstanceType": "BASIC",
            "NetworkConfig": {
                "InternetMaxBandwidthOut": 10,
                "EnableInternetInbound": true,
                "EnableInternetOutbound": true,
                "InboundIpAddresses": [
                    "10.10.10.10"
                ],
                "OutboundIpAddresses": [
                    "10.10.10.11"
                ]
            },
            "VpcConfig": {
                "UniqVpcId": "vpc-12345",
                "UniqSubnetId": "subnet-12345"
            },
            "Parameters": [
                {
                    "Name": "ServiceRequestNumPreSec",
                    "Value": 500,
                    "Default": 500,
                    "Unit": "次/秒",
                    "Type": "integer",
                    "Minimum": 0,
                    "Maximum": 500,
                    "ModifedTime": "2018-10-30T04:24:19"
                }
            ],
            "IsolationStartedTime": "2018-10-30T04:24:19Z",
            "CreatedTime": "2018-10-30T04:24:19Z"
        },
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

