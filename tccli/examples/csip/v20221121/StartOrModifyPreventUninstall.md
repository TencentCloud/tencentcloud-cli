**Example 1: 开启或者修改防卸载功能**



Input: 

```
tccli csip StartOrModifyPreventUninstall --cli-unfold-argument  \
    --From 1 \
    --Scope 1 \
    --MemberId mem-tencent-e74488e0ba0cd8fe \
    --IncludeQuuid 829fdf0d-b8d8-431e-9f96-ed54a143edff \
    --ExcludeQuuid 829fdf0d-b8d8-431e-9f96-ed54a143edff
```

Output: 
```
{
    "Response": {
        "FailList": [],
        "FailedHostCount": 1,
        "TaskId": 0,
        "RequestId": "aadebac7-940a-48c6-b2b6-0d88d3f7db3f"
    }
}
```

