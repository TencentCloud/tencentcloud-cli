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
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.2,
                "UnitPriceThirdStep": 0.1,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.06,
                "UnitPriceSecondStep": 0.12,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.06,
                "UnitPriceDiscount": 0.08,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            },
            "BandwidthPrice": {
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.0,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.0,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            }
        },
        "RequestId": "65b9edac-bca6-496b-a404-29f503b32495"
    }
}
```

**Example 2: 包年包月实例购买询价**

实例所在位置为上海二区，付费模式为包年包月，购买一个月，到期自动续费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码未Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceCount 1 \
    --Placement.Zone ap-shanghai-2 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7 \
    --InstanceChargeType PREPAID \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceName QCLOUD-TEST \
    --InstanceType S5.16XLARGE256 \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "DiscountPrice": 1804.9,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.0,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 8884.5,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.0,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            },
            "BandwidthPrice": {
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.8,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.52,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            }
        },
        "RequestId": "65b9edac-bca6-496b-a404-29f503b32495"
    }
}
```

**Example 3: 按小时后付费实例购买询价**

实例所在位置为上海二区，付费模式为按小时后付费，镜像ID为：img-pmqg1cw7，选择机型为：64C256G标准型(S5.16XLARGE256)，50G大小高性能云系统盘，挂载100G大小高性能云数据盘，私有网络，公网付费模式为流量按小时后付费，外网带宽上限10Mbps，分配公网IP，实例命名为QCLOUD-TEST，设置登录密码未Qcloud@TestApi123++，安装云监控云安全，购买数量为1台。

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --InstanceCount 1 \
    --Placement.Zone ap-shanghai-2 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE \
    --InternetAccessible.PublicIpAssigned TRUE \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 10 \
    --InstanceName QCLOUD-TEST \
    --InstanceType S5.16XLARGE256 \
    --DataDisks.0.DiskSize 100 \
    --DataDisks.0.DiskType CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 16.09,
                "UnitPriceThirdStep": 16.09,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 3.33,
                "UnitPriceSecondStep": 16.09,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 3.33,
                "UnitPriceDiscount": 3.33,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            },
            "BandwidthPrice": {
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.8,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.52,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "xx",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            }
        },
        "RequestId": "65b9edac-bca6-496b-a404-29f503b32495"
    }
}
```

