**Example 1: 实例一**

查询子用户策略

Input: 

```
tccli dlc DescribeSubUserAccessPolicy --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PolicyDocument": "{\"statement\":[{\"action\":[\"cos:*\"],\"effect\":\"allow\",\"resource\":[\"qcs::cos:ap-beijing:uid/123456:test_bucket/*\",\"qcs::cos:ap-beijing:uid/123456:test_bucket/*\",\"qcs::cos:ap-beijing:uid/123456:test_bucket/*\"]}],\"version\":\"2.0\"}",
        "RequestId": "799cd718-d0da-4f7c-a0c1-104205dc6d8f"
    }
}
```

