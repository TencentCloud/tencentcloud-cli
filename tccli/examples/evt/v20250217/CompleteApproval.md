**Example 1: 完成审批任务**



Input: 

```
tccli evt CompleteApproval --cli-unfold-argument  \
    --ApprovalId A202507150000000000000 \
    --NodeId AN202507150000000000000 \
    --Result 1 \
    --Opinion 通过
```

Output: 
```
{
    "Response": {
        "RequestId": "a057f127-ee97-43fc-9b60-07cd420c1111"
    }
}
```

