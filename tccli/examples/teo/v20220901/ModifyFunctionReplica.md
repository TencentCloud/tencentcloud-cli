**Example 1: 编辑边缘函数副本**

修改函数ID为 ef-crkwnfy0 的边缘函数下的一个名为 Hello-World-Replica 的边缘函数副本的内容和描述。

Input: 

```
tccli teo ModifyFunctionReplica --cli-unfold-argument  \
    --ZoneId zone-3exa7oergn0l \
    --FunctionId ef-crkwnfy0 \
    --ReplicaName Hello-World-Replica \
    --Content addEventListener('fetch', e => {
  const response = new Response('Hello World 2!');
  e.respondWith(response);
}); \
    --Remark Hello World Replica
```

Output: 
```
{
    "Response": {
        "RequestId": "58b4ccab-3ce0-4e2a-a832-93c88eeb3c71"
    }
}
```

