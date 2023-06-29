**Example 1: 查询部门-查询单个部门**

查询部门-查询单个部门

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --QueryType 0 \
    --DeptId yDwgIUUckp1gxxxxxxxxE8xOm12b9
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "yDwgIUUckp1gxxxxxxxxE8xOm12b9",
                "DeptName": "测试企业",
                "DeptOpenId": "open_dept1",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1gxxxxxxxxE8xOm1221"
            }
        ],
        "RequestId": "s168603XXXXXXX44722"
    }
}
```

**Example 2: 查询部门-查询当前部门和一级子部门**

查询部门-查询当前部门和一级子部门

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --QueryType 1 \
    --DeptId yDwgIUUckp1gxxxxxxxxE8xOm12b9
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "yDwgIUUckp1gxxxxxxxxE8xOm12b9",
                "DeptName": "测试企业",
                "DeptOpenId": "open_dept1",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1gxxxxxxxxE8xOm1221"
            },
            {
                "DeptId": "yDwgIUUckp1gxxxxxxxxE8xOm5679",
                "DeptName": "AAAAA",
                "DeptOpenId": "12347",
                "OrderNo": 3,
                "ParentDeptId": "yDwgIUUckp1gxxxxxxxxE8xOm12b9"
            },
            {
                "DeptId": "yDwgIU2331gxxxxxxxxE8xOm12n9",
                "DeptName": "BBBBB",
                "DeptOpenId": "12344",
                "OrderNo": 2,
                "ParentDeptId": "yDwgIUUckp1gxxxxxxxxE8xOm12b9"
            }
        ],
        "RequestId": "s168603XXXXXXX44722"
    }
}
```

