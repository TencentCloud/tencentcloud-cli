**Example 1: 创建环境角色关系映射**



Input: 

```
tccli tdmq CreateEnvironmentRole --cli-unfold-argument  \
    --EnvironmentId devDemo \
    --RoleName role1 \
    --Permissions produce \
    --ClusterId pulsar-xk3ne8k2qkp8
```

Output: 
```
{
    "Response": {
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

