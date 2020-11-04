**Example 1: 获取可用区的机型配置信息列表**

通过可用区和付费类型作为过滤条件, 查询配置信息列表。

Input: 

```
tccli cvm DescribeZoneInstanceConfigInfos --cli-unfold-argument  \
    --Filters.0.Name zone\
    --Filters.0.Values ap-guangzhou-2\
    --Filters.1.Name instance-charge-type\
    --Filters.1.Values POSTPAID_BY_HOUR
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
                    "UnitPrice": 0.15,
                    "DiscountThirdStep": "100.000000",
                    "UnitPriceThirdStep": 0.05,
                    "DiscountSecondStep": "100.000000",
                    "Discount": "100.000000",
                    "UnitPriceDiscountThirdStep": 0.05,
                    "UnitPriceSecondStep": 0.07,
                    "UnitPriceDiscount": 0.15,
                    "UnitPriceDiscountSecondStep": 0.07,
                    "ChargeUnit": "HOUR"
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
                "Fpga": 0,
                "Remark": ""
            }
        ],
        "RequestId": "c28559ca-d3cf-40f0-9664-2ab303484efa"
    }
}
```

