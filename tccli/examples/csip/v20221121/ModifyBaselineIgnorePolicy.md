**Example 1: 添加忽略策略**

添加忽略策略

Input: 

```
tccli csip ModifyBaselineIgnorePolicy --cli-unfold-argument  \
    --ItemID 1 \
    --ScopeType ALL \
    --ScopeIncludeList instance-tki \
    --ScopeExcludeList instance-ikj \
    --Remark ignore all \
    --ID 0 \
    --MemberId mem-tencent-6f5795752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "f2dec187-04f4-4cd2-aeb1-ce51c56bc8b8"
    }
}
```

