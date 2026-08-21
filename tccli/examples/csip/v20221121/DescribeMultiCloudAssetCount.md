**Example 1: 获取多云资产数量**



Input: 

```
tccli csip DescribeMultiCloudAssetCount --cli-unfold-argument  \
    --MemberId mem-*******-**************29
```

Output: 
```
{
    "Response": {
        "TotalCount": 256,
        "CloudAssetInfos": [
            {
                "CloudType": "tencent",
                "Count": 120
            },
            {
                "CloudType": "aliyun",
                "Count": 86
            },
            {
                "CloudType": "aws",
                "Count": 50
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

