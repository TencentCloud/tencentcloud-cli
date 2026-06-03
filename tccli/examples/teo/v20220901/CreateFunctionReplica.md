**Example 1: 创建边缘函数副本**

为函数ID为 ef-crkwnfy0 的边缘函数添加一个名为 Hello-World-Replica 的边缘函数副本，创建副本后可通过添加请求头 EO-Function-Replica-Name: "Hello-World-Replica" 访问该副本的函数。

Input: 

```
tccli teo CreateFunctionReplica --cli-unfold-argument  \
    --ZoneId zone-3exa7oergn0l \
    --FunctionId ef-crkwnfy0 \
    --ReplicaName Hello-World-Replica \
    --Content addEventListener('fetch', e => {
  const response = new Response('Hello World!');
  e.respondWith(response);
}); \
    --Remark Hello World Replica
```

Output: 
```
{
    "Response": {
        "RequestId": "176711aa-10e2-4573-b3ee-b4fbdac2780f"
    }
}
```

