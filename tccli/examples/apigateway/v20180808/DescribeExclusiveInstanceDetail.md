**Example 1: DescribeExclusiveInstanceDetail**

查询独享实例详情

Input: 

```
tccli apigateway DescribeExclusiveInstanceDetail --cli-unfold-argument  \
    --InstanceId instance-90v2ohwp
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceId": "abc",
            "Zone": "abc",
            "InstanceName": "abc",
            "InstanceDescription": "abc",
            "InstanceChargeType": "abc",
            "InstanceState": "abc",
            "InstanceChargePrepaid": {
                "RenewFlag": "abc",
                "ExpiredTime": "2020-09-22T00:00:00+00:00"
            },
            "InstanceType": "abc",
            "NetworkConfig": {
                "InternetMaxBandwidthOut": 0,
                "EnableInternetInbound": true,
                "EnableInternetOutbound": true,
                "InboundIpAddresses": [
                    "abc"
                ],
                "OutboundIpAddresses": [
                    "abc"
                ]
            },
            "VpcConfig": {
                "UniqVpcId": "abc",
                "UniqSubnetId": "abc"
            },
            "Parameters": [
                {
                    "Name": "abc",
                    "Value": 0,
                    "Default": 0,
                    "Unit": "abc",
                    "Type": "abc",
                    "Minimum": 0,
                    "Maximum": 0,
                    "ModifedTime": "2020-09-22T00:00:00+00:00",
                    "ValueString": "abc",
                    "DefaultValueString": "abc",
                    "Range": "abc"
                }
            ],
            "IsolationStartedTime": "2020-09-22T00:00:00+00:00",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "Zones": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

