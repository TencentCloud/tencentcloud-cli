**Example 1: 终止演练**



Input: 

```
tccli cfg ModifyTaskRunStatus --cli-unfold-argument  \
    --Status 1004 \
    --IsExpect True \
    --TaskId 222 \
    --Summary 演习结论
```

Output: 
```
{
    "Response": {
        "RequestId": "e38eca72-e4ae-4a86-9696-7df399e672bd"
    }
}
```

**Example 2: 示例1**



Input: 

```
tccli cfg ModifyTaskRunStatus --cli-unfold-argument  \
    --Status 1002 \
    --TaskId 1698
```

Output: 
```
{
    "Response": {
        "RequestId": "8e9a0777-ff96-4020-8aec-6802d8103689"
    }
}
```

