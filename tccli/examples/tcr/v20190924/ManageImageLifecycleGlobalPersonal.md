**Example 1: 设置个人版全局镜像版本清理策略**



Input: 

```
tccli tcr ManageImageLifecycleGlobalPersonal --cli-unfold-argument  \
    --Type global_keep_last_nums \
    --Val 9998
```

Output: 
```
{
    "Response": {
        "RequestId": "fdc10ec8-a1cf-4c2a-8eb4-f6d66abfdd53"
    }
}
```

