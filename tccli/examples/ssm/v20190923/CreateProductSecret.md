**Example 1: 创建云产品凭据**



Input: 

```
tccli ssm CreateProductSecret --cli-unfold-argument  \
    --SecretName testName \
    --UserNamePrefix testPrefix \
    --ProductName Mysql \
    --InstanceID cdb-vosgis \
    --Description test \
    --KmsKeyId 2609a8fd-4584-4f89-98be-8c7ae1b81ef4 \
    --RotationBeginTime '2006-01-02 15:04:05' \
    --EnableRotation true \
    --RotationFrequency 35 \
    --Domains % \
    --Tags.0.TagKey tagKey \
    --Tags.0.TagValue tagVal \
    --PrivilegesList.0.PrivilegeName object \
    --PrivilegesList.0.Privileges read \
    --PrivilegesList.0.Database testdb \
    --PrivilegesList.0.TableName testtable \
    --PrivilegesList.0.ColumnName testColumn
```

Output: 
```
{
    "Response": {
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4",
        "SecretName": "testName",
        "TagCode": 0,
        "TagMsg": "success",
        "FlowID": 123
    }
}
```

