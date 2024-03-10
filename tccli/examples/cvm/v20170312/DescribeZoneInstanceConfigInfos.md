**Example 1: 获取可用区的机型配置信息列表**

通过可用区和付费类型作为过滤条件, 查询配置信息列表。

Input: 

```
tccli cvm DescribeZoneInstanceConfigInfos --cli-unfold-argument  \
    --Filters.0.Values POSTPAID_BY_HOUR \
    --Filters.0.Name instance-charge-type \
    --Filters.1.Values ap-guangzhou-2 \
    --Filters.1.Name zone
```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Status": "SELL",
                "Zone": "ap-guangzhou-2",
                "NetworkCard": 0,
                "Price": {
                    "DiscountPrice": 59,
                    "OriginalPriceThreeYear": 0,
                    "DiscountOneYear": 0,
                    "UnitPrice": 0,
                    "UnitPriceThirdStep": 0,
                    "OriginalPriceFiveYear": 0,
                    "Discount": 0,
                    "DiscountFiveYear": 0,
                    "UnitPriceDiscountThirdStep": 0,
                    "UnitPriceSecondStep": 0,
                    "OriginalPrice": 59,
                    "DiscountThreeYear": 0,
                    "UnitPriceDiscountSecondStep": 0,
                    "UnitPriceDiscount": 0,
                    "DiscountPriceFiveYear": 0,
                    "OriginalPriceOneYear": 708,
                    "ChargeUnit": "HOUR",
                    "DiscountPriceThreeYear": 0,
                    "DiscountPriceOneYear": 587.64
                },
                "InstanceFamily": "S2",
                "Externals": {},
                "InstanceType": "S2.SMALL1",
                "TypeName": "Standard S2",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "Memory": 1,
                "LocalDiskTypeList": [],
                "Cpu": 1,
                "SoldOutReason": "",
                "StorageBlockAmount": 0,
                "CpuType": "Intel Xeon E5-2680 v4",
                "InstancePps": 20,
                "InstanceBandwidth": 1.5,
                "Gpu": 0,
                "GpuCount": 0,
                "Fpga": 0,
                "Remark": "",
                "Frequency": "2.4GHz",
                "StatusCategory": "EnoughStock"
            }
        ],
        "RequestId": "c28559ca-d3cf-40f0-9664-2ab303484efa"
    }
}
```

