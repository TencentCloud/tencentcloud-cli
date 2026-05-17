**Example 1: 查看风险证据以及描述**



Input: 

```
tccli csip DescribeCosRiskEvidence --cli-unfold-argument  \
    --RelAppId 122321414 \
    --PolicyId 1 \
    --BucketName brain-122321414
```

Output: 
```
{
    "Response": {
        "RequestId": "req-123456789",
        "Total": 1,
        "Evidences": [
            {
                "PermissionSource": "CAM",
                "PermissionContent": "{\"Version\":\"2.0\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"QCS\":[\"qcs::cam::uin/100000000001:uin/100000000001\"]},\"Action\":[\"name/cos:GetObject\",\"name/cos:PutObject\"],\"Resource\":[\"qcs::cos:ap-beijing:uid/100000000001:my-bucket/*\"]}]}",
                "GrantResource": "qcs::cos:ap-beijing:uid/100000000001:my-bucket/*",
                "GrantAction": "name/cos:GetObject,name/cos:PutObject",
                "GrantCondition": "{\"StringEquals\":{\"cos:prefix\":\"example/\"}}"
            },
            {
                "PermissionSource": "Bucket Policy",
                "PermissionContent": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"PublicReadGetObject\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::my-bucket/*\"}]}",
                "GrantResource": "arn:aws:s3:::my-bucket/*",
                "GrantAction": "s3:GetObject",
                "GrantCondition": "{\"StringEquals\":{\"aws:Referer\":\"https://example.com\"}}"
            },
            {
                "PermissionSource": "ACL",
                "PermissionContent": "{\"Owner\":{\"ID\":\"qcs::cam::uin/100000000001:uin/100000000001\"},\"Grants\":[{\"Grantee\":{\"Type\":\"Group\",\"URI\":\"http://acs.amazonaws.com/groups/global/AllUsers\"},\"Permission\":\"READ\"}]}",
                "GrantResource": "my-bucket",
                "GrantAction": "READ",
                "GrantCondition": ""
            },
            {
                "PermissionSource": "CAM",
                "PermissionContent": "{\"Version\":\"2.0\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"QCS\":[\"qcs::cam::uin/100000000002:uin/100000000002\"]},\"Action\":[\"name/cos:DeleteObject\"],\"Resource\":[\"qcs::cos:ap-shanghai:uid/100000000002:prod-bucket/*\"]}]}",
                "GrantResource": "qcs::cos:ap-shanghai:uid/100000000002:prod-bucket/*",
                "GrantAction": "name/cos:DeleteObject",
                "GrantCondition": "{\"StringEquals\":{\"cos:prefix\":\"temp/\"}}"
            },
            {
                "PermissionSource": "Bucket Policy",
                "PermissionContent": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"FullAccess\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:user/test-user\"},\"Action\":\"s3:*\",\"Resource\":[\"arn:aws:s3:::prod-bucket\",\"arn:aws:s3:::prod-bucket/*\"]}]}",
                "GrantResource": "arn:aws:s3:::prod-bucket/*",
                "GrantAction": "s3:*",
                "GrantCondition": "{\"StringEquals\":{\"aws:SourceIp\":\"192.168.1.0/24\"}}"
            }
        ]
    }
}
```

