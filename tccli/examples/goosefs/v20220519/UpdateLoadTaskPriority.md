**Example 1: 修改目标预热任务优先级**



Input: 

```
tccli goosefs UpdateLoadTaskPriority --cli-unfold-argument  \
    --ClusterId g_cvm_36brs5g2 \
    --TaskId 2c4a3356-28d5-4f87-98c3-78745b5d6bbf \
    --Priority 666
```

Output: 
```
{
    "Response": {
        "RequestId": "2650658c-e716-4ba0-b96a-2f9cfbcb5cb1"
    }
}
```

