**Example 1: 创建部门**

创建部门，指定父部门ID，部门被创建至父部门节点下。

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

**Example 2: 创建部门-不指定父部门ID**

创建部门，不指定父部门ID，部门被创建至根部门节点下。

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc************QZDRuD \
    --DeptName 运营部 \
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

**Example 3: 创建部门-同时指定第三方平台与电子签父部门ID**

创建部门，同时指定第三方平台与电子签父部门ID，系统优先使用电子签平台部门ID。

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc************QZDRuD \
    --DeptName 运营部 \
    --ParentDeptId yDwgIUUckp1g**********E8xOm12b9 \
    --ParentDeptOpenId dept_1 \
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

**Example 4: 错误示例-参数不合法**

调用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不合法，接口将返回错误信息。

Input: 

```
tccli ess CreateIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc************QZDRuD \
    --DeptName 运营部11111111111111111111111111111111111111111111111111111 \
    --ParentDeptId yDwgIUUckp1g**********E8xOm12b9 \
    --DeptOpenId open_dept2 \
    --OrderNo 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "部门名称请控制在50个字符以内"
        },
        "RequestId": "914axxxx-xxxx-xxxx-xxxx-xxxxxxxx70123"
    }
}
```

