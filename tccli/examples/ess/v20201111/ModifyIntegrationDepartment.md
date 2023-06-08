**Example 1: 更新部门**

更新部门

Input: 

```
tccli ess ModifyIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId XXXXXX \
    --DeptName 运营部 \
    --DeptId XXXXXXXXXXXXX \
    --DeptOpenId xxx \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "RequestId": "s1679xxxxx21175"
    }
}
```

