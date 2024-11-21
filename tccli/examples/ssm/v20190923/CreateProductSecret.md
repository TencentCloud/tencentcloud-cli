**Example 1: 创建云产品凭据**

CreateProductSecret创建云产品凭据请求示例

Input: 

```
tccli ssm CreateProductSecret --cli-unfold-argument  \
    --SecretName test3-db-secret \
    --UserNamePrefix lzctest \
    --ProductName Mysql \
    --InstanceID cdb-n4j3y33j \
    --Domains % \
    --PrivilegesList.0.PrivilegeName GlobalPrivileges \
    --PrivilegesList.0.Privileges SELECT \
    --Description 测试数据库凭据创建 \
    --KmsKeyId 6abd1fdb-86d4-11ef-b72d-52540089bc41 \
    --Tags.0.TagKey env \
    --Tags.0.TagValue dev \
    --RotationBeginTime 2024-10-31 11:11:00 \
    --EnableRotation True \
    --RotationFrequency 30
```

Output: 
```
{
    "Response": {
        "FlowID": 43415,
        "RequestId": "0f5fa585-7671-4d4a-bc28-41910b772936",
        "SecretName": "test3-db-secret",
        "TagCode": 0,
        "TagMsg": "ok"
    }
}
```

