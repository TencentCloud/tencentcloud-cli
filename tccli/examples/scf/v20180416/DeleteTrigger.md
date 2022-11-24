**Example 1: 删除触发器**

用户使用该函数删除触发器。

Input: 

```
tccli scf DeleteTrigger --cli-unfold-argument  \
    --Type timer \
    --FunctionName ledDummyAPITest \
    --TriggerName test3
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

