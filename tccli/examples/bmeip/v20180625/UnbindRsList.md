**Example 1: 批量解绑物理机EIP相关接口**



Input: 

```
tccli bmeip UnbindRsList --cli-unfold-argument  \
    --EipRsList.0.EipId eip-pq9cuew0 \
    --EipRsList.0.InstanceId cpm-s1hf4voq
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

