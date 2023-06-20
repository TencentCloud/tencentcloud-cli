**Example 1: 创建部门**

创建部门

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --DeptName 运营部 \
    --ParentDeptId yDwgIUUckp1gxxxxxxxxE8xOm12b9 \
    --DeptOpenId open_dept2 \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "DeptId": "yDwgIUUckp1gxxxxxxxxE8xOm1567",
        "RequestId": "s1679xxxxx21175"
    }
}
```

