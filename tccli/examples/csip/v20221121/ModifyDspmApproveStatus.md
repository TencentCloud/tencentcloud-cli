**Example 1: 修改Dspm审批单状态**



Input: 

```
tccli csip ModifyDspmApproveStatus --cli-unfold-argument  \
    --OrderId order-6wfo0fzks3 \
    --Status 1 \
    --Comment 
```

Output: 
```
{
    "Response": {
        "RequestId": "45ca21d4-f373-4274-9295-5380abc74bed"
    }
}
```

