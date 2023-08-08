**Example 1: 创建部门**

创建部门

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc************QZDRuD \
    --DeptName 运营部 \
    --ParentDeptId yDwgIUUckp1g**********E8xOm12b9 \
    --DeptOpenId open_dept2 \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "DeptId": "yDwgIUUckp1g********E8xOm1567",
        "RequestId": "s1679*****21175"
    }
}
```

