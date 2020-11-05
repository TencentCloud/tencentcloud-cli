**Example 1: Modifying security group bound to TencentDB instance**



Input: 

```
tccli cdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceId cdb-eb2w7dto\
    --SecurityGroupIds sg-ajr1jzgj
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

