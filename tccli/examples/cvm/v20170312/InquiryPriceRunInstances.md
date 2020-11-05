**Example 1: Querying the price of a pay-as-you-go instance billed on an hourly basis**

This example shows you how to query the price for purchasing one 64C256G standard (S5.16XLARGE256) instance in Shanghai Zone 2 using the image `img-pmqg1cw7`. The other configurations are as follows: system disk: 50 GB Premium Cloud Storage; data disk: 100 GB Premium Cloud Storage; network type: VPC; public network billing: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 10 Mbps; public IP: randomly assigned; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; Cloud Monitoring service: enabled; Anti-DDoS: enabled.

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2\
    --InstanceChargeType POSTPAID_BY_HOUR\
    --ImageId img-pmqg1cw7\
    --InstanceType S5.16XLARGE256\
    --SystemDisk.DiskType CLOUD_PREMIUM\
    --SystemDisk.DiskSize 50\
    --DataDisks.0.DiskType CLOUD_PREMIUM\
    --DataDisks.0.DiskSize 100\
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR\
    --InternetAccessible.InternetMaxBandwidthOut 10\
    --InternetAccessible.PublicIpAssigned TRUE\
    --InstanceName QCLOUD-TEST\
    --LoginSettings.Password Qcloud@TestApi123++\
    --EnhancedService.SecurityService.Enabled TRUE\
    --EnhancedService.MonitorService.Enabled TRUE\
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalInstanceTypePrice": 15.95,
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

**Example 2: Querying the price of an instance with only the required parameters**

This example shows you how to create an instance using only the required `Placement.Zone` and `ImageId` parameters. The other parameters use system default values. The instance is created in Shanghai Zone 2 with image `img-pmqg1cw7`.

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2\
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalInstanceTypePrice": 0.15,
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

**Example 3: Querying the price of a monthly subscription instance**

This example shows you how to query the price for purchasing one 64C256G standard (S5.16XLARGE256) instance in Shanghai Zone 2 using the image `img-pmqg1cw7`. The other configurations are as follows: billing method: monthly subscription for one month with auto-renewal upon expiration; system disk: 50 GB Premium Cloud Storage; data disk: 100 GB Premium Cloud Storage; network type: VPC; public network billing: pay-as-you-go by traffic on an hourly basis; public network bandwidth cap: 10 Mbps; public IP: randomly assigned; instance name: QCLOUD-TEST; login password: Qcloud@TestApi123++; Cloud Monitoring service: enabled; Anti-DDoS: enabled.

Input: 

```
tccli cvm InquiryPriceRunInstances --cli-unfold-argument  \
    --Placement.Zone ap-shanghai-2\
    --InstanceChargeType PREPAID\
    --InstanceChargePrepaid.Period 1\
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW\
    --ImageId img-pmqg1cw7\
    --InstanceType S5.16XLARGE256\
    --SystemDisk.DiskType CLOUD_PREMIUM\
    --SystemDisk.DiskSize 50\
    --DataDisks.0.DiskType CLOUD_PREMIUM\
    --DataDisks.0.DiskSize 100\
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR\
    --InternetAccessible.InternetMaxBandwidthOut 10\
    --InternetAccessible.PublicIpAssigned TRUE\
    --InstanceName QCLOUD-TEST\
    --LoginSettings.Password Qcloud@TestApi123++\
    --EnhancedService.SecurityService.Enabled TRUE\
    --EnhancedService.MonitorService.Enabled TRUE\
    --InstanceCount 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "DiscountPrice": 1804.9,
                "OriginalInstanceTypePrice": 8832,
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

