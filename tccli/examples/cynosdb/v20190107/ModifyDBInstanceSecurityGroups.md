**Example 1: 修改云数据库安全组**

修改安全组

Input: 

```
tccli cynosdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId abc \
    --SecurityGroupIds abc \
    --Zone abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

