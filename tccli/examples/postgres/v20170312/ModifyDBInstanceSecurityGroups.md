**Example 1: 修改安全组**

修改安全组。

Input: 

```
tccli postgres ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --DBInstanceId postgres-i2q4utnp \
    --SecurityGroupIdSet sg-91jbmkp1
```

Output: 
```
{
    "Response": {
        "RequestId": "5fad142d-9597-408f-84b8-41a27a1486ce"
    }
}
```

**Example 2: 修改只读实例组安全组**

修改只读实例组安全组。

Input: 

```
tccli postgres ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --ReadOnlyGroupId pgrogrp-nqwpkjb \
    --SecurityGroupIdSet sg-91jbmkp1
```

Output: 
```
{
    "Response": {
        "RequestId": "f81495e4-bca8-4946-b5b0-0aedc512413d"
    }
}
```

