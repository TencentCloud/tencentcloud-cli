**Example 1: 物理机解绑EIP**



Input: 

```
tccli bmeip UnbindRs --cli-unfold-argument  \
    --EipId 字符串 \
    --InstanceId 字符串
```

Output: 
```
{
    "Response": {
        "TaskId": 2488348,
        "RequestId": "ebef4926-8982-45b6-be53-e09b3baa4ab7"
    }
}
```

