**Example 1: 查询镜像授权信息**



Input: 

```
tccli tcss DescribeImageAuthorizedInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ScannedImageCnt": 1,
        "TotalAuthorizedCnt": 1,
        "NotScannedLocalImageCnt": 1,
        "RequestId": "xx",
        "UsedAuthorizedCnt": 1,
        "NotScannedImageCnt": 1
    }
}
```

