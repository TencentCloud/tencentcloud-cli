**Example 1: 预付费标准版2.0-2次防护-1IP-业务带宽10Mbps**



Input: 

```
tccli antiddos CreateBgpInstance --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --PackageType StandardPlus \
    --InstanceCount 1 \
    --InstanceChargePrepaid.Period 3 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --StandardPlusPackageConfig.Region ap-guangzhou \
    --StandardPlusPackageConfig.ProtectCount TWO_TIMES \
    --StandardPlusPackageConfig.ProtectIpCount 1 \
    --StandardPlusPackageConfig.Bandwidth 10 \
    --StandardPlusPackageConfig.ElasticBandwidthFlag True \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "bgp-00000451"
        ],
        "RequestId": "fe8e9c34-a2c0-4bb2-a874-2b7386adbd97"
    }
}
```

**Example 2: 预付费模式-广州地域-标准版购买10M-1IP**



Input: 

```
tccli antiddos CreateBgpInstance --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --PackageType Standard \
    --InstanceCount 1 \
    --InstanceChargePrepaid.Period 3 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --StandardPackageConfig.Region ap-guangzhou \
    --StandardPackageConfig.ProtectIpCount 1 \
    --StandardPackageConfig.Bandwidth 10 \
    --StandardPackageConfig.ElasticBandwidthFlag True \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "bgp-0000043i"
        ],
        "RequestId": "e122a577-1266-4193-b223-f8cb654b5209"
    }
}
```

**Example 3: 预付费模式-购买企业版高防包-保底带宽300Gbps业务带宽10Mbps防护IP数1**



Input: 

```
tccli antiddos CreateBgpInstance --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --PackageType Enterprise \
    --InstanceCount 1 \
    --InstanceChargePrepaid.Period 3 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --EnterprisePackageConfig.Region ap-guangzhou \
    --EnterprisePackageConfig.ProtectIpCount 1 \
    --EnterprisePackageConfig.BasicProtectBandwidth 300 \
    --EnterprisePackageConfig.Bandwidth 10 \
    --EnterprisePackageConfig.ElasticBandwidthFlag True \
    --TagInfoList.0.TagKey beal-test \
    --TagInfoList.0.TagValue beal-test \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "bgp-00000450"
        ],
        "RequestId": "dc81b4ff-730a-4907-a2eb-b08fc1e1e8b8"
    }
}
```

**Example 4: 后付费标准版防护IP10 业务带宽100Mbps**



Input: 

```
tccli antiddos CreateBgpInstance --cli-unfold-argument  \
    --InstanceChargeType POSTPAID_BY_MONTH \
    --PackageType Standard \
    --InstanceCount 1 \
    --StandardPackageConfig.Region ap-shanghai \
    --StandardPackageConfig.ProtectIpCount 10 \
    --StandardPackageConfig.Bandwidth 100 \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "bgp-000004ku"
        ],
        "RequestId": "340d95e7-4ea2-480c-958b-ca094141911f"
    }
}
```

