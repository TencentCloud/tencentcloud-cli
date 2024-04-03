**Example 1: 修改实例postgres-6ougo465名字，修改失败**

修改实例名称失败。

Input: 

```
tccli postgres ModifyDBInstanceName --cli-unfold-argument  \
    --InstanceName testModifyInstanceName \
    --DBInstanceId postgres-6ougo465
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61f510-aa33-454c-9ec2-dq2a368c39ab",
        "Error": {
            "Message": "Failed to get instance",
            "Code": "InternalError.DBError"
        }
    }
}
```

**Example 2: 将实例postgres-6fego161名字修改为testModifyInstanceName**

修改实例名称为testModifyInstanceName。

Input: 

```
tccli postgres ModifyDBInstanceName --cli-unfold-argument  \
    --InstanceName testModifyInstanceName \
    --DBInstanceId postgres-6fego161
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab"
    }
}
```

