**Example 1: 查询镜像授权信息**



Input: 

```
tccli tcss DescribeImageAuthorizedInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CanApplyFreeImageAuthorize": false,
        "ImageScanInquireInfo": {
            "Capcity": 18601,
            "EndTime": "2024-12-24 13:01:18",
            "InquireKey": "sv_yunjing_cssil_image",
            "PurchaseStatus": "Normal",
            "ResourceID": "427c59056cbd64e30b3990e8d7b25c19",
            "StartTime": "2024-09-24 13:01:18",
            "Useage": 17365
        },
        "NotScannedImageCnt": 38,
        "NotScannedLocalImageCnt": 12,
        "PurchasedAuthorizedCnt": 300000,
        "RepeatImageIdCnt": 2,
        "RequestId": "0ad4465e-cf84-411f-bd10-75bbb3a9c9aa",
        "ScannedImageCnt": 11687,
        "TotalAuthorizedCnt": 300000,
        "TrialAuthorizedCnt": 0,
        "UsedAuthorizedCnt": 300000,
        "UsedPurchasedAuthorizedCnt": 300000,
        "UsedTrialAuthorizedCnt": 0
    }
}
```

