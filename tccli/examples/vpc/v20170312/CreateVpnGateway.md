**Example 1: Creating a monthly-subscribed gateway**



Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-5rkcp0wb\
    --VpnGatewayName TEST_PREPAID_VPNGW\
    --InstanceChargeType PREPAID\
    --InternetMaxBandwidthOut 5\
    --InstanceChargePrepaid.Period 1\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpnGatewayId": "vpngw-97yhzme3",
            "VpcId": "vpc-5rkcp0wb",
            "VpnGatewayName": "TEST_PREPAID_VPNGW",
            "State": "Pending",
            "InstanceChargeType": "PREPAID",
            "Type": "IPSEC"
        },
        "RequestId": "7e553bb7-5603-4b79-a9f5-ecfe37d9eb27"
    }
}
```

**Example 2: Creating a pay-as-you-go gateway**



Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcId vpc-ngenl4az\
    --VpnGatewayName TEST_POSTPAID_VPNGW\
    --InstanceChargeType POSTPAID_BY_HOUR\
    --InternetMaxBandwidthOut 5\
    --Tags.0.Key city\
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpnGatewayId": "vpngw-rn2yn85v",
            "VpcId": "vpc-ngenl4az",
            "VpnGatewayName": "TEST_POSTPAID_VPNGW",
            "State": "Pending",
            "InstanceChargeType": "POSTPAID_BY_HOUR",
            "Type": "IPSEC"
        },
        "RequestId": "1dede54a-bbad-4d7b-9110-c7cb1ed7c152"
    }
}
```

