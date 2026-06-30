**Example 1: 创建用户组**



Input: 

```
tccli clb CreateUserGroup --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --UserGroupName 核心业务组 \
    --Models deepseek-v3 \
    --IntentRouters ir-chat
```

Output: 
```
{
    "Response": {
        "UserGroupId": "ugrp-9f8e7d6c",
        "RequestId": "d81e7b1f-3587-491b-8556-9e47222fecfd"
    }
}
```

