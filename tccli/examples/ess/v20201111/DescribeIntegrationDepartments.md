**Example 1: 查询单个部门信息**

适用于需要查询指定部门信息，且不需要子部门信息的场景。
1. 设置查询类型QueryType为0表示查询单个部门节点；
2. 设置DeptId表示通过部门ID查询相关部门信息。

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

**Example 2: 错误示例-部门查询类型不存在**

设置了非法的部门查询类型QueryType，查询失败。

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcX******XQZDRuD \
    --QueryType 2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "部门查询类型不存在，请核对参数"
        },
        "RequestId": "s168603******44722"
    }
}
```

**Example 3: 查询当前部门和一级子部门信息**

适用于需要查询指定部门及其一级子部门信息的场景。
1. 设置查询类型QueryType为1表示查询部门节点及一级子部门节点；
2. 设置DeptId表示通过部门ID查询相关部门信息。

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

**Example 4: 查询部门信息（根据客户系统部门ID）**

适用于调用方已获取客户系统部门ID的场景。通过设置DeptOpenId参数查询部门信息。

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcX******XQZDRuD \
    --QueryType 0 \
    --DeptOpenId open_dept1
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

**Example 5: 查询部门信息（系统优先使用部门ID查询）**

当调用方同时设置了部门DeptId和客户系统部门DeptOpenId时，系统优先使用DeptId查询部门信息，DeptOpenId不生效。

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcX******XQZDRuD \
    --QueryType 0 \
    --DeptId yDwgIUUckp1g*****E8xOm12b9 \
    --DeptOpenId open_dept2
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

**Example 6: 查询部门信息（系统默认返回根部门节点信息）**

当部门DeptId和客户系统部门DeptOpenId都未设置时，系统默认返回根部门节点信息。

Input: 

```
tccli ess DescribeIntegrationDepartments --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcX******XQZDRuD \
    --QueryType 0
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
                "OrderNo": 0,
                "ParentDeptId": "0"
            }
        ],
        "RequestId": "s168603******44722"
    }
}
```

