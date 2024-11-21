**Example 1: 修改高危系统调用事件状态**



Input: 

```
tccli tcss ModifyRiskSyscallStatus --cli-unfold-argument  \
    --EventIdSet 61c396cb85a03485f10c353e \
    --Status EVENT_INGNORE \
    --Remark 备注
```

Output: 
```
{
    "Response": {
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

