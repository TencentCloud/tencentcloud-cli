**Example 1: 启动函数debug版本**



Input: 

```
tccli scf CreateDebugVersion --cli-unfold-argument  \
    --FunctionName debug-test-v2 \
    --Namespace zed \
    --StartCommand sleep infinity \
    --PersistenceTime 60
```

Output: 
```
{
    "Response": {
        "RequestId": "928ec139-ad8d-4b32-a0f4-012017606e28"
    }
}
```

