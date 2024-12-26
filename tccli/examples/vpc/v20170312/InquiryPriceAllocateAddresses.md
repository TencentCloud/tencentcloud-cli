**Example 1: 小时流量计费模式弹性公网IP询价**

小时流量计费模式弹性公网IP询价。

Input: 

```
tccli vpc InquiryPriceAllocateAddresses --cli-unfold-argument  \
    --AddressType EIP \
    --InternetMaxBandwidthOut 1 \
    --InternetChargeType TRAFFIC_POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "ChargeUnit": "HOUR",
                "UnitPrice": 0.8,
                "DiscountPrice": 0.8
            }
        },
        "RequestId": "90d508a8-9ee8-4220-9c8e-9faeedce3ab4"
    }
}
```

**Example 2: 小时带宽计费模式弹性公网IP询价**

小时带宽计费模式弹性公网IP询价。

Input: 

```
tccli vpc InquiryPriceAllocateAddresses --cli-unfold-argument  \
    --AddressType EIP \
    --InternetMaxBandwidthOut 1 \
    --InternetChargeType BANDWIDTH_POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "UnitPrice": 0.063,
                "DiscountPrice": 0.063,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "ebc826be-ec1a-4522-b08f-8da3fe5adedc"
    }
}
```

**Example 3: 包月带宽计费模式弹性公网IP询价**

包月带宽计费模式弹性公网IP询价。

Input: 

```
tccli vpc InquiryPriceAllocateAddresses --cli-unfold-argument  \
    --AddressChargePrepaid.Period 1 \
    --AddressType EIP \
    --InternetChargeType BANDWIDTH_PREPAID_BY_MONTH \
    --InternetMaxBandwidthOut 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "OriginalPrice": 20,
                "DiscountPrice": 20
            }
        },
        "RequestId": "136605f0-ca35-4d22-9b77-e053168fa25f"
    }
}
```

