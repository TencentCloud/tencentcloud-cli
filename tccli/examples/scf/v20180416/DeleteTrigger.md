**Example 1: 删除触发器**

用户使用该函数删除触发器。

Input: 

```
tccli scf DeleteTrigger --cli-unfold-argument  \
    --FunctionName ledDummyAPITest\
    --TriggerName test3\
    --Type timer
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

