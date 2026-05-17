**Example 1: 查看风险关联的存储桶信息**



Input: 

```
tccli csip DescribeRiskBucketList --cli-unfold-argument  \
    --RelAppId 137182812 \
    --PolicyId rule-1qazxsw2
```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Data": [
            {
                "AppId": 123456789,
                "BucketName": "my-bucket",
                "BucketRegion": "ap-beijing",
                "BucketUin": "100000000001",
                "BucketNickName": "测试用户",
                "BucketMainNickName": "主账号用户",
                "BucketIdentify": 1,
                "LastScanTimestamp": 1705293000,
                "HandleStatus": 0
            },
            {
                "AppId": 123456789,
                "BucketName": "prod-bucket",
                "BucketRegion": "ap-shanghai",
                "BucketUin": "100000000002",
                "BucketNickName": "生产用户",
                "BucketMainNickName": "主账号用户",
                "BucketIdentify": 2,
                "LastScanTimestamp": 1705296000,
                "HandleStatus": 1
            },
            {
                "AppId": 123456789,
                "BucketName": "test-bucket",
                "BucketRegion": "ap-guangzhou",
                "BucketUin": "100000000003",
                "BucketNickName": "子账号用户",
                "BucketMainNickName": "主账号用户",
                "BucketIdentify": 3,
                "LastScanTimestamp": 1705299000,
                "HandleStatus": 0
            },
            {
                "AppId": 123456789,
                "BucketName": "backup-bucket",
                "BucketRegion": "ap-chengdu",
                "BucketUin": "100000000004",
                "BucketNickName": "备份用户",
                "BucketMainNickName": "主账号用户",
                "BucketIdentify": 1,
                "LastScanTimestamp": 1705302000,
                "HandleStatus": 2
            }
        ],
        "Total": 4
    }
}
```

