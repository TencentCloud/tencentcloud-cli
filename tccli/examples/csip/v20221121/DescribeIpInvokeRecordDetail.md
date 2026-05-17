**Example 1: ip访问列表详情信息**



Input: 

```
tccli csip DescribeIpInvokeRecordDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e",
        "InvokeDetailInfo": [
            {
                "InvokeTimestamp": 1705293000,
                "InvokeRequestId": "req-123456789",
                "InvokeContent": "{\"Action\":\"GetObject\",\"Bucket\":\"my-bucket\",\"Key\":\"example/file.txt\",\"VersionId\":\"null\"}"
            },
            {
                "InvokeTimestamp": 1705296000,
                "InvokeRequestId": "req-123456790",
                "InvokeContent": "{\"Action\":\"PutObject\",\"Bucket\":\"my-bucket\",\"Key\":\"example/upload.txt\",\"Content-Length\":\"1024\"}"
            },
            {
                "InvokeTimestamp": 1705299000,
                "InvokeRequestId": "req-123456791",
                "InvokeContent": "{\"Action\":\"ListObjects\",\"Bucket\":\"my-bucket\",\"Prefix\":\"example/\",\"MaxKeys\":\"1000\"}"
            }
        ],
        "InvokePermission": [
            {
                "PermissionSource": "CAM",
                "PermissionContent": "{\"Version\":\"2.0\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"QCS\":[\"qcs::cam::uin/100000000001:uin/100000000001\"]},\"Action\":[\"name/cos:GetObject\"],\"Resource\":[\"qcs::cos:ap-beijing:uid/100000000001:my-bucket/*\"]}]}",
                "GrantResource": "qcs::cos:ap-beijing:uid/100000000001:my-bucket/*",
                "GrantAction": "name/cos:GetObject",
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
            }
        ]
    }
}
```

