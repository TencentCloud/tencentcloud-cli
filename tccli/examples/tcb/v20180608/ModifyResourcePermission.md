**Example 1: 修改sql数据库表的基础权限**

修改数据库表users的权限为READONLY（读取全部数据，修改本人数据）

Input: 

```
tccli tcb ModifyResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType table \
    --Resource users \
    --Permission READONLY
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "8ab60429-c2a2-45fd-b458-1add52a5473c"
    }
}
```

**Example 2: 修改文档型数据库表的基础权限**

修改文档型数据库表testte的基础权限为ADMINWRITE。

Input: 

```
tccli tcb ModifyResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType collection \
    --Permission ADMINWRITE \
    --Resource testte
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "34b64585-bd0e-45ba-850d-8c950078fdf7"
    }
}
```

**Example 3: 修改云函数的安全规则**

修改云函数的安全规则为全部可调用

Input: 

```
tccli tcb ModifyResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType function \
    --Permission CUSTOM \
    --SecurityRule {
    "*": {
        "invoke": true    }
}
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "85a3896c-3237-4f8a-b78a-b15328b49e1d"
    }
}
```

**Example 4: 修改云存储桶的基础权限**

修改云存储桶的基础权限为PRIVATE。

Input: 

```
tccli tcb ModifyResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType storage \
    --Permission PRIVATE \
    --Resource or*
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true
        },
        "RequestId": "6035aeb1-0840-4de9-8a0d-eee85803a893"
    }
}
```

