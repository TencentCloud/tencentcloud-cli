**Example 1: 查询部门-查询单个部门**

查询部门-查询单个部门

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcX******XQZDRuD \
    --QueryType 0 \
    --DeptId yDwgIUUckp1g******E8xOm12b9
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "yDwgIUUckp1g*****E8xOm12b9",
                "DeptName": "测试企业",
                "DeptOpenId": "open_dept1",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1g******E8xOm1221"
            }
        ],
        "RequestId": "s168603******44722"
    }
}
```

**Example 2: 查询部门-查询当前部门和一级子部门**

查询部门-查询当前部门和一级子部门

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc********QZDRuD \
    --QueryType 1 \
    --DeptId yDwgIUUckp1g******E8xOm12b9
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "yDwgIUUckp1g********E8xOm12b9",
                "DeptName": "测试企业",
                "DeptOpenId": "open_dept1",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1g********E8xOm1221"
            },
            {
                "DeptId": "yDwgIUUckp1g********E8xOm5679",
                "DeptName": "子部门 1",
                "DeptOpenId": "open_dept_12",
                "OrderNo": 3,
                "ParentDeptId": "yDwgIUUckp1g*******E8xOm12b9"
            },
            {
                "DeptId": "yDwgIU2331g********E8xOm12n9",
                "DeptName": "测试部门 2",
                "DeptOpenId": "open_dept_13",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1g********E8xOm12b9"
            }
        ],
        "RequestId": "s168603******44722"
    }
}
```

