**Example 1: 修改实例安全组**

修改实例安全组

Input: 

```
tccli tdmysql ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId tdsql3-be88fd7f \
    --SecurityGroupIds sg-bbu5xxm3
```

Output: 
```
{
    "Response": {
        "RequestId": "dab65c4d-b0c3-427f-b39e-3323606bba06"
    }
}
```

