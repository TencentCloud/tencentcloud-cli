**Example 1: 创建按量计费网关**



Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --VpcId vpc-ngenl4az \
    --VpnGatewayName TEST_POSTPAID_VPNGW \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InternetMaxBandwidthOut 5 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpcId": "vpc-ngenl4az",
            "VpnGatewayId": "vpngw-test1234",
            "VpnGatewayName": "TEST_POSTPAID_VPNGW",
            "Type": "IPSEC",
            "State": "AVAILABLE",
            "PublicIpAddress": "xxx.xxx.xxx.xxx",
            "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
            "InstanceChargeType": "POSTPAID_BY_HOUR",
            "InternetMaxBandwidthOut": 5,
            "CreatedTime": "2020-10-13 19:03:26",
            "ExpiredTime": "2020-12-13 19:04:54",
            "IsAddressBlocked": false,
            "NewPurchasePlan": "",
            "RestrictState": "NORMAL",
            "Zone": "ap-shanghai-1",
            "Version": "ver2.0",
            "NetworkInstanceId": "vpc-i9otxqn5",
            "VpnGatewayQuotaSet": [
                {
                    "Bandwidth": 5,
                    "Cname": "微小型",
                    "Name": "qcmini"
                },
                {
                    "Bandwidth": 50,
                    "Cname": "大型",
                    "Name": "qclarge"
                },
                {
                    "Bandwidth": 200,
                    "Cname": "超大型2",
                    "Name": "qcsuperLarge2"
                },
                {
                    "Bandwidth": 100,
                    "Cname": "超大型",
                    "Name": "qcsuperLarge"
                },
                {
                    "Bandwidth": 500,
                    "Cname": "超大型3",
                    "Name": "qcsuperLarge3"
                },
                {
                    "Bandwidth": 10,
                    "Cname": "小型",
                    "Name": "qcsmall"
                },
                {
                    "Bandwidth": 20,
                    "Cname": "中型",
                    "Name": "qcmiddle"
                },
                {
                    "Bandwidth": 1000,
                    "Cname": "超大型4",
                    "Name": "qcsuperLarge4"
                }
            ]
        },
        "RequestId": "ea4bc0de-5093-423e-96ae-08f0fd4889be"
    }
}
```

**Example 2: 创建包年包月网关**



Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --VpcId vpc-5rkcp0wb \
    --VpnGatewayName TEST_PREPAID_VPNGW \
    --InstanceChargeType PREPAID \
    --InternetMaxBandwidthOut 5 \
    --InstanceChargePrepaid.Period 1 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpcId": "vpc-5rkcp0wb",
            "VpnGatewayId": "vpngw-test1234",
            "VpnGatewayName": "TEST_PREPAID_VPNGW",
            "Type": "IPSEC",
            "State": "AVAILABLE",
            "PublicIpAddress": "xxx.xxx.xxx.xxx",
            "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
            "InstanceChargeType": "PREPAID",
            "InternetMaxBandwidthOut": 5,
            "CreatedTime": "2020-10-13 19:03:26",
            "ExpiredTime": "2020-12-13 19:04:54",
            "IsAddressBlocked": false,
            "NewPurchasePlan": "",
            "RestrictState": "NORMAL",
            "Zone": "ap-shanghai-1",
            "Version": "ver2.0",
            "NetworkInstanceId": "vpc-i9otxqn5",
            "VpnGatewayQuotaSet": [
                {
                    "Bandwidth": 5,
                    "Cname": "微小型",
                    "Name": "qcmini"
                },
                {
                    "Bandwidth": 50,
                    "Cname": "大型",
                    "Name": "qclarge"
                },
                {
                    "Bandwidth": 200,
                    "Cname": "超大型2",
                    "Name": "qcsuperLarge2"
                },
                {
                    "Bandwidth": 100,
                    "Cname": "超大型",
                    "Name": "qcsuperLarge"
                },
                {
                    "Bandwidth": 500,
                    "Cname": "超大型3",
                    "Name": "qcsuperLarge3"
                },
                {
                    "Bandwidth": 10,
                    "Cname": "小型",
                    "Name": "qcsmall"
                },
                {
                    "Bandwidth": 20,
                    "Cname": "中型",
                    "Name": "qcmiddle"
                },
                {
                    "Bandwidth": 1000,
                    "Cname": "超大型4",
                    "Name": "qcsuperLarge4"
                }
            ]
        },
        "RequestId": "ea4bc0de-5093-423e-96ae-08f0fd4889be"
    }
}
```

