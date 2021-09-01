**Example 1: 按量付费实例调整带宽上限询价**

对实例ins-fd8spnmq调整带宽为20Mbps进行询价

Input: 

```
tccli cvm InquiryPriceResetInstancesInternetMaxBandwidth --cli-unfold-argument  \
    --InstanceIds ins-fd8spnmq \
    --InternetAccessible.InternetMaxBandwidthOut 20
```

Output: 
```
{
    "Response": {
        "Price": {
            "BandwidthPrice": {
                "UnitPrice": 0.8,
                "ChargeUnit": "GB"
            }
        },
        "RequestId": "700864b9-85da-4cb9-bc80-d99eaf9fa047"
    }
}
```

