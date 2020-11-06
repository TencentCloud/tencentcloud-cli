**Example 1: 设置个人版全局镜像版本清理策略**



Input: 

```
tccli tcr ManageImageLifecycleGlobalPersonal --cli-unfold-argument  \
    --Type keep_last_nums \
    --Val 80
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

