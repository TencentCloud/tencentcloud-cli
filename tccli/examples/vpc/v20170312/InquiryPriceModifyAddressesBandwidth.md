**Example 1: 小时流量EIP修改带宽询价**

小时流量EIP修改带宽询价。

Input: 

```
tccli vpc InquiryPriceModifyAddressesBandwidth --cli-unfold-argument  \
    --InternetMaxBandwidthOut 2 \
    --AddressIds eip-hxlqja90
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "UnitPrice": 0.8,
                "DiscountPrice": 0.8,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "7daad6af-50de-4df5-8238-0d76c7be62e1"
    }
}
```

**Example 2: 小时带宽EIP修改带宽询价**

小时带宽EIP修改带宽询价。

Input: 

```
tccli vpc InquiryPriceModifyAddressesBandwidth --cli-unfold-argument  \
    --AddressIds eip-3hwtklhj \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "UnitPrice": 0.315,
                "DiscountPrice": 0.315,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "db071565-27cb-482a-a3fe-1c7bba77e4a9"
    }
}
```

**Example 3: 包月带宽EIP调整带宽询价**

包月带宽EIP调整带宽询价。

Input: 

```
tccli vpc InquiryPriceModifyAddressesBandwidth --cli-unfold-argument  \
    --AddressIds eip-iu4ml5pp \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "OriginalPrice": 95,
                "DiscountPrice": 95
            }
        },
        "RequestId": "ddf8edf2-0457-4ba7-b2ab-e66e98823cc6"
    }
}
```

