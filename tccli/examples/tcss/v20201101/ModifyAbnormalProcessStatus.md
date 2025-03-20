**Example 1: 修改异常进程事件状态**



Input: 

```
tccli tcss ModifyAbnormalProcessStatus --cli-unfold-argument  \
    --EventIdSet 10001 \
    --Status ' EVENT_DEALED' \
    --Remark Remark
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

