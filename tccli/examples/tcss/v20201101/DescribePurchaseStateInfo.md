**Example 1: 查询容器安全服务已购买信息**



Input: 

```
tccli tcss DescribePurchaseStateInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AuthorizedImageCnt": 1,
        "PurchasedAuthorizedCnt": 1,
        "GivenAuthorizedCnt": 500,
        "AuthorizedCoresCnt": 1,
        "ImageCnt": 1,
        "State": 4,
        "RequestId": "xx",
        "ExpirationTime": "xx",
        "CoresCnt": 1,
        "AutomaticRenewal": 0,
        "BeginTime": "xx",
        "SubState": "ISOLATE"
    }
}
```

