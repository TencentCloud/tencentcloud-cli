**Example 1: 创建环境角色关系映射**



Input: 

```
tccli tdmq CreateEnvironmentRole --cli-unfold-argument  \
    --RoleName test_role_1 \
    --EnvironmentId default \
    --Permissions produce
```

Output: 
```
{
    "Response": {
        "RequestId": "gggxxxx"
    }
}
```

