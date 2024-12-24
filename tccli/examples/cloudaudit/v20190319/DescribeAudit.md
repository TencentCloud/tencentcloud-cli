**Example 1: 查询跟踪集详情**

查询跟踪集详情

Input: 

```
tccli cloudaudit DescribeAudit --cli-unfold-argument  \
    --AuditName xxxxx_cloudaudit_2
```

Output: 
```
{
    "Response": {
        "AuditName": "xxxxx_cloudaudit_2",
        "CmqQueueName": "xxxxx-cloudaudit-2",
        "CmqRegion": "hk",
        "CosBucketName": "xxxxx-cloudaudit-2",
        "CosRegion": "ap-hongkong",
        "IsEnableCmqNotify": 1,
        "LogFilePrefix": "xxx2312",
        "ReadWriteAttribute": 1,
        "AuditStatus": 1,
        "KeyId": "34",
        "IsEnableKmsEncry": 0,
        "KmsRegion": "hk",
        "KmsAlias": "cloudtrail",
        "RequestId": "e23ee347-d011-482a-83fa-12e7d318dd9f"
    }
}
```

