**Example 1: 查询容器安全服务已购买信息**



Input: 

```
tccli tcss DescribePurchaseStateInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "State": 0,
        "CoresCnt": 1,
        "AuthorizedCoresCnt": 1,
        "ImageCnt": 1,
        "AuthorizedImageCnt": 1,
        "PurchasedAuthorizedCnt": 1,
        "ExpirationTime": "abc",
        "AutomaticRenewal": 0,
        "GivenAuthorizedCnt": 1,
        "BeginTime": "abc",
        "SubState": "abc",
        "InquireKey": "abc",
        "RequestId": "abc"
    }
}
```

