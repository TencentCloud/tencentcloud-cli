**Example 1: 查询闪信记录列表**

查询闪信记录列表

Input: 

```
tccli ccc DescribeFlashSMSList --cli-unfold-argument  \
    --SdkAppId 1500098920 \
    --StartTimestamp 1769730111 \
    --EndTimestamp 1769749111 \
    --SessionId 15adb830-****-****-****-20c7d825d845 \
    --DeliveryNumber 00860755******88 \
    --ServingNumber 0086021******07
```

Output: 
```
{
    "Response": {
        "FlashSMSList": [
            {
                "ArriveTimestamp": 1769738753,
                "DeliveryMessage": "success",
                "DeliveryNumber": "0086158******69",
                "DeliveryStatus": 1,
                "DeliveryTimestamp": 1769738751,
                "ServingNumber": "0086021******07",
                "SessionId": "b6801264-****-****-****-8ffd29033e32"
            }
        ],
        "Total": 1,
        "RequestId": "3e9a5b29-5d5c-491b-885c-05f3ea6c3b0e"
    }
}
```

