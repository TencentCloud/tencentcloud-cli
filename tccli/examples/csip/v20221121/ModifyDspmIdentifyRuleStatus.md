**Example 1: 修改dspm数据识别数据项状态**



Input: 

```
tccli csip ModifyDspmIdentifyRuleStatus --cli-unfold-argument  \
    --Ids 10356 \
    --Status 0 \
    --MemberId mem-12ed1we1
```

Output: 
```
{
    "Response": {
        "RequestId": "5f7d5d3d-c628-4e6e-8eb0-a39042ce791b"
    }
}
```

