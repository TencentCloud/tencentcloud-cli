**Example 1: 修改环境角色授权**



Input: 

```
tccli tdmq ModifyEnvironmentRole --cli-unfold-argument  \
    --RoleName test_role \
    --EnvironmentId default \
    --Permissions produce consume
```

Output: 
```
{
    "Response": {
        "RequestId": "gggxxxx"
    }
}
```

