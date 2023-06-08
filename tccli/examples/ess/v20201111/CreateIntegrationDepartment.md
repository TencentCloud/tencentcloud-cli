**Example 1: 创建部门**

创建部门

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId XXXXXX \
    --DeptName 运营部 \
    --ParentDeptId XXXXXXXXXXXXX \
    --DeptOpenId xxx \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "DeptId": "XXXXXXXXXXXXXXXX",
        "RequestId": "s1679xxxxx21175"
    }
}
```

