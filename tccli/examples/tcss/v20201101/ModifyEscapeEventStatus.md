**Example 1: 修改容器逃逸扫描事件状态**



Input: 

```
tccli tcss ModifyEscapeEventStatus --cli-unfold-argument  \
    --Status EVENT_IGNORE \
    --EventIdSet 33705186
```

Output: 
```
{
    "Response": {
        "RequestId": "3c3b5c8a-727b-4e32-b679-bcb5d6530c67"
    }
}
```

