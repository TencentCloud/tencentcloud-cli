**Example 1: 查询部门-查询单个部门**

查询部门-查询单个部门

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId XXXXXX \
    --QueryType 0 \
    --DeptId XXXXXXXXXXXXXXX
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "XXXXXXXXXXXXXXX",
                "DeptName": "测试企业",
                "DeptOpenId": "xxx",
                "OrderNo": 2,
                "ParentDeptId": "xxxxx"
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
    --Operator.UserId XXXXXX \
    --QueryType 1 \
    --DeptId XXXXXXXXXXXXXXX
```

Output: 
```
{
    "Response": {
        "Departments": [
            {
                "DeptId": "XXXXXXXXXXXXXXX",
                "DeptName": "测试企业",
                "DeptOpenId": "xxx",
                "OrderNo": 2,
                "ParentDeptId": "xxxxx"
            },
            {
                "DeptId": "AAAAA",
                "DeptName": "AAAAA",
                "DeptOpenId": "12347",
                "OrderNo": 3,
                "ParentDeptId": "XXXXXXXXXXXXXXX"
            },
            {
                "DeptId": "BBBBB",
                "DeptName": "BBBBB",
                "DeptOpenId": "12344",
                "OrderNo": 2,
                "ParentDeptId": "XXXXXXXXXXXXXXX"
            }
        ],
        "RequestId": "s168603XXXXXXX44722"
    }
}
```

