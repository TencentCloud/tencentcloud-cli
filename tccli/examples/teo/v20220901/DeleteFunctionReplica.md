**Example 1: 删除边缘函数副本**

删除站点 ID 为 zone-3exa7oergn0l 下边缘函数 ID 为 ef-crkwnfy0 函数副本名称为 Hello-World-Replica 的边缘函数副本。

Input: 

```
tccli teo DeleteFunctionReplica --cli-unfold-argument  \
    --ZoneId zone-3exa7oergn0l \
    --FunctionId ef-crkwnfy0 \
    --ReplicaNames Hello-World-Replica
```

Output: 
```
{
    "Response": {
        "RequestId": "ed746f01-805b-474c-b020-9db1898a7302"
    }
}
```

