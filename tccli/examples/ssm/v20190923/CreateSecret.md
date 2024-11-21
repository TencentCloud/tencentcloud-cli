**Example 1: 创建新的凭据信息**

创建自定义凭据。

Input: 

```
tccli ssm CreateSecret --cli-unfold-argument  \
    --SecretName test3_secret \
    --VersionId v2.0 \
    --Description 测试自定义凭据创建 \
    --KmsKeyId 6abd1fdb-86d4-11ef-b72d-52540089bc41 \
    --SecretType 0 \
    --SecretString 凭据value2
```

Output: 
```
{
    "Response": {
        "RequestId": "be7d863d-8d8d-4d28-97b7-3dad7236bb33",
        "SecretName": "test2_secret",
        "TagCode": 0,
        "TagMsg": "ok",
        "VersionId": "v2.0"
    }
}
```

