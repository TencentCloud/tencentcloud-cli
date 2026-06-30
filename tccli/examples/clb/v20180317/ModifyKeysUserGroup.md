**Example 1: 批量入组**



Input: 

```
tccli clb ModifyKeysUserGroup --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --UserGroupId ugrp-9f8e7d6c \
    --KeyIds mkey-aaa111 mkey-bbb222
```

Output: 
```
{
    "Response": {
        "RequestId": "d81e7b1f-3587-491b-8556-9e47222fecfd"
    }
}
```

**Example 2: 批量移出到未分组**



Input: 

```
tccli clb ModifyKeysUserGroup --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --UserGroupId ugrp-ungrouped \
    --KeyIds mkey-aaa111
```

Output: 
```
{
    "Response": {
        "RequestId": "d81e7b1f-3587-491b-8556-9e47222fecfd"
    }
}
```

