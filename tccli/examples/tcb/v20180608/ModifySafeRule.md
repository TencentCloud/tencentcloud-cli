**Example 1: 修改安全规则为私有读写**

将环境ID:myenv-c849jgkdldcmsd 下，文档型数据库(数据表 blogs) 的安全规则，调整为私有读写（PRIVATE，仅创建者可读写）

Input: 

```
tccli tcb ModifySafeRule --cli-unfold-argument  \
    --EnvId myenv-c849jgkdldcmsd \
    --CollectionName blogs \
    --AclTag PRIVATE
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

