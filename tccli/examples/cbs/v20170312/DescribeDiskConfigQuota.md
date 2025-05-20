**Example 1: 查询上海五区高性能云硬盘的可售卖规格**

查询上海五区高性能云硬盘的可售卖规格

Input: 

```
tccli cbs DescribeDiskConfigQuota --cli-unfold-argument  \
    --InquiryType INQUIRY_CBS_CONFIG \
    --DiskChargeType POSTPAID_BY_HOUR \
    --Zones ap-shanghai-5 \
    --DiskTypes CLOUD_PREMIUM
```

Output: 
```
{
    "Response": {
        "DiskConfigSet": [
            {
                "Available": true,
                "MaxDiskSize": 32000,
                "Zone": "ap-shanghai-5",
                "InstanceFamily": null,
                "DiskType": "CLOUD_PREMIUM",
                "StepSize": 1,
                "ExtraPerformanceRange": null,
                "DeviceClass": null,
                "DiskUsage": "DATA_DISK",
                "MinDiskSize": 10,
                "DiskChargeType": "PREPAID",
                "Price": {
                    "DiscountPriceHigh": "81",
                    "DiscountPrice": 1.0,
                    "UnitPriceHigh": "1.00",
                    "UnitPriceDiscountHigh": "1.00",
                    "OriginalPriceHigh": "10",
                    "ChargeUnit": "H",
                    "OriginalPrice": 1.0,
                    "UnitPriceDiscount": 0.21,
                    "UnitPrice": 0.21
                }
            }
        ],
        "RequestId": "50346458-c053-47f1-b60f-5507e7cc5b26"
    }
}
```

