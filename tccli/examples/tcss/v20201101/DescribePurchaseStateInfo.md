**Example 1: 查询容器安全服务已购买信息**



Input: 

```
tccli tcss DescribePurchaseStateInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllCoresCnt": 154,
        "AuthorizedCoresCnt": 147,
        "AuthorizedImageCnt": 287756,
        "AutomaticRenewal": 194,
        "BeginTime": "2024-09-24 13:01:18",
        "CoresCnt": 68,
        "CurrentFlexibleCoresCnt": 0,
        "DefendClusterCoresCnt": 48,
        "DefendHostCoresCnt": 20,
        "DefendPolicy": "Part",
        "ExpirationTime": "2024-12-24 13:01:18",
        "FlexibleCoresLimit": 5000,
        "GivenAuthorizedCnt": 0,
        "GivenAuthorizedCoresCnt": 0,
        "ImageCnt": 291209,
        "InquireKey": "sv_yunjing_css_pem",
        "PurchasedAuthorizedCnt": 300000,
        "RequestId": "e40cad09-f295-42a8-914d-ea84767fb6f1",
        "State": 3,
        "SubState": "NORMAL",
        "UndefendCoresCnt": 86,
        "TrialCoresCnt": 0
    }
}
```

