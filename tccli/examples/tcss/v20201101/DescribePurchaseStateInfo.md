**Example 1: 查询容器安全服务已购买信息**



Input: 

```
tccli tcss DescribePurchaseStateInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "State": 0,
        "AllCoresCnt": 1,
        "CoresCnt": 1,
        "UndefendCoresCnt": 1,
        "AuthorizedCoresCnt": 1,
        "GivenAuthorizedCoresCnt": 0,
        "CurrentFlexibleCoresCnt": 1,
        "ImageCnt": 1,
        "AuthorizedImageCnt": 1,
        "ExpirationTime": "abc",
        "PurchasedAuthorizedCnt": 1,
        "AutomaticRenewal": 0,
        "GivenAuthorizedCnt": 1,
        "BeginTime": "abc",
        "SubState": "abc",
        "InquireKey": "abc",
        "DefendPolicy": "abc",
        "FlexibleCoresLimit": 1,
        "DefendClusterCoresCnt": 1,
        "DefendHostCoresCnt": 1,
        "RequestId": "abc"
    }
}
```

