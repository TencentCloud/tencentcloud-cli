**Example 1: 修改企业安全组下发状态**

修改企业安全组下发状态

Input: 

```
tccli cfw ModifyEnterpriseSecurityDispatchStatus --cli-unfold-argument  \
    --Status 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "b21d7f7c-3191-41a2-bd13-9a5f6d86ab44"
    }
}
```

