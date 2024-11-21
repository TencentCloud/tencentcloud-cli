**Example 1: 创建角色**

创建角色

Input: 

```
tccli tdmq CreateRole --cli-unfold-argument  \
    --RoleName devName \
    --Remark devRemark \
    --ClusterId pulsar-xk3ne8k2qkp8
```

Output: 
```
{
    "Response": {
        "RoleName": "devName",
        "Token": "ajdsaiuasdnmasllamm",
        "Remark": "devRemark",
        "EnvironmentRoleSets": [
            {
                "EnvironmentId": "devNs",
                "Permissions": [
                    "produce"
                ]
            }
        ],
        "RequestId": "1004f1de-6fb8-41d5-965e-3aae8c87183a"
    }
}
```

