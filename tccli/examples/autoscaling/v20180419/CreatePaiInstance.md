**Example 1: 创建单个PAI实例**

通过指定的域名等参数，创建单个PAI实例

Input: 

```
tccli as CreatePaiInstance --cli-unfold-argument  \
    --DomainName apple-gz012345.pai.tcloudbase.com \
    --InitScript IyEvYmluL2Jhc2gKZWNobyAiaGVsbG8iCg \
    --Zones ap-guangzhou-2 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InstanceTypes S4.SMALL2 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceName PAI-TEST \
    --LoginSettings.Password PAI@Test123
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-bmmk7d75"
        ],
        "RequestId": "843518b0-43bb-4066-a00b-d95b338b3142"
    }
}
```

