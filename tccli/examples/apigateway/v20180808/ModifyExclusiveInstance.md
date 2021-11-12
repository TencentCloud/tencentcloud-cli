**Example 1: ModifyExclusiveInstance**



Input: 

```
tccli apigateway ModifyExclusiveInstance --cli-unfold-argument  \
    --InstanceId instance-crbytkvwas
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
                {}
            ],
            "IsolationStartedTime": "2020-09-22T00:00:00+00:00",
            "CreatedTime": "2018-10-30T04:24:19Z"
        },
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

