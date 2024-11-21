**Example 1: 修改运行时访问控制事件状态**



Input: 

```
tccli tcss ModifyAccessControlStatus --cli-unfold-argument  \
    --EventIdSet 10001 \
    --Status EVENT_DEALED \
    --Remark 无
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

