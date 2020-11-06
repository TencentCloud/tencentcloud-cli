**Example 1: Querying the price of a pay-as-you-go instance with a new bandwidth cap**

This example shows you how to query the price for changing the bandwidth of the instance “ins-fd8spnmq” to 20 Mbps.

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

