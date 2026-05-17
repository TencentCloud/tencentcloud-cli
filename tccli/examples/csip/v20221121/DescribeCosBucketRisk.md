**Example 1: 查看风险资产视角**



Input: 

```
tccli csip DescribeCosBucketRisk --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Data": [
            {
                "RiskId": 10,
                "AppId": 123456789,
                "BucketName": "test-bucket",
                "BucketRegion": "ap-guangzhou",
                "BucketMarker": "测试存储桶",
                "BucketAccessWay": "specify",
                "BucketUin": "100000000003",
                "BucketNickName": "子账号用户",
                "BucketMainNickName": "主账号用户",
                "BucketTagInfo": "[{\"Key\":\"Value\"}]",
                "BucketIdentify": 3,
                "LastScanTimestamp": 1705299000,
                "HandleStatus": 0,
                "PolicyName": "COS异常访问检测",
                "PolicyType": 3,
                "PolicyId": 1,
                "PolicyLevel": 1,
                "PolicyDescription": "风险问题命中"
            }
        ],
        "Total": 5
    }
}
```

