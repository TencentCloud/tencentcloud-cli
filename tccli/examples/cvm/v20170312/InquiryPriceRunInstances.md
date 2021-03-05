**Example 1: 最简单参数的购买询价**

只传必传的Zone和镜像ID，其他均采用系统默认值，具体配置如下：实例所在位置为上海二区，镜像ID为：img-pmqg1cw7。

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.2,
                "UnitPriceThirdStep": 0.1,
                "Discount": 40,
                "UnitPriceDiscountThirdStep": 0.06,
                "UnitPriceSecondStep": 0.12,
                "UnitPriceDiscount": 0.08,
                "UnitPriceDiscountSecondStep": 0.06,
                "ChargeUnit": "HOUR"
            },
            "BandwidthPrice": {
                "ChargeUnit": "GB",
                "UnitPrice": 0,
                "Discount": 65,
                "UnitPriceDiscount": 0
            }
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 包年包月实例购买询价**

实例所在位置为上海二区，付费模式为包年包月，购买一个月，到期自动续费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码未Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --InstanceChargeType PREPAID \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --ImageId img-pmqg1cw7 \
    --InstanceType S5.16XLARGE256 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InstanceName QCLOUD-TEST \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "DiscountPrice": 1804.9,
                "OriginalPrice": 8884.5,
                "Discount": 20
            },
            "BandwidthPrice": {
                "ChargeUnit": "GB",
                "UnitPrice": 0.8,
                "UnitPriceDiscount": 0.52,
                "Discount": 65
            }
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: 按小时后付费实例购买询价**

实例所在位置为上海二区，付费模式为按小时后付费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码未Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --ImageId img-pmqg1cw7 \
    --InstanceType S5.16XLARGE256 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 50 \
    --DataDisks.0.DiskType CLOUD_PREMIUM \
    --DataDisks.0.DiskSize 100 \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InstanceName QCLOUD-TEST \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 16.09,
                "UnitPriceThirdStep": 16.09,
                "Discount": 21,
                "UnitPriceDiscountThirdStep": 3.33,
                "UnitPriceSecondStep": 16.09,
                "UnitPriceDiscount": 3.33,
                "UnitPriceDiscountSecondStep": 3.33,
                "ChargeUnit": "HOUR"
            },
            "BandwidthPrice": {
                "ChargeUnit": "GB",
                "UnitPrice": 0.8,
                "Discount": 65,
                "UnitPriceDiscount": 0.52
            }
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

