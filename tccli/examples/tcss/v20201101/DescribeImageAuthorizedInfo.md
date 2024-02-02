**Example 1: 查询镜像授权信息**



Input: 

```
tccli tcss DescribeImageAuthorizedInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalAuthorizedCnt": 1,
        "UsedAuthorizedCnt": 1,
        "ScannedImageCnt": 1,
        "NotScannedImageCnt": 1,
        "NotScannedLocalImageCnt": 1,
        "TrialAuthorizedCnt": 1,
        "UsedTrialAuthorizedCnt": 1,
        "PurchasedAuthorizedCnt": 1,
        "UsedPurchasedAuthorizedCnt": 1,
        "CanApplyFreeImageAuthorize": true,
        "RequestId": "abc"
    }
}
```

