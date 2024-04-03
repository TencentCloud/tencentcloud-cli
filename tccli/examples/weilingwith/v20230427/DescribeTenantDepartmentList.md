**Example 1: 组织部门列表**

组织部门列表

Input: 

```
tccli weilingwith DescribeTenantDepartmentList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --DepartmentId 6 \
    --ApplicationToken zD3G1qtO9Fy4mu5HAMydrXNHBputBQVS
```

Output: 
```
{
    "Response": {
        "RequestId": "86a86966-f838-44ec-b1e4-469429cf0b61",
        "Result": {
            "Departments": [
                {
                    "DepartmentId": "32",
                    "Name": "外部测试",
                    "ParentDepartmentId": "6"
                }
            ],
            "Total": 2
        }
    }
}
```

**Example 2: 查询组织部门列表**

查询组织部门列表

Input: 

```
tccli weilingwith DescribeTenantDepartmentList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --DepartmentId 6 \
    --ApplicationToken zD3G1qtO9Fy4mu5HAMydrXNHBputBQVS
```

Output: 
```
{
    "Response": {
        "RequestId": "3e2b7483-9dc0-48af-8d5a-95bebecef8c3",
        "Result": {
            "Departments": [
                {
                    "DepartmentId": "32",
                    "Name": "外部测试",
                    "ParentDepartmentId": "6"
                }
            ],
            "Total": 2
        }
    }
}
```

**Example 3: 查询租户组织部门列表**

查询租户组织部门列表

Input: 

```
tccli weilingwith DescribeTenantDepartmentList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --DepartmentId 6 \
    --ApplicationToken zD3G1qtO9Fy4mu5HAMydrXNHBputBQVS
```

Output: 
```
{
    "Response": {
        "RequestId": "fbb81f22-548b-43e9-afad-08c595058205",
        "Result": {
            "Departments": [
                {
                    "DepartmentId": "32",
                    "Name": "外部测试",
                    "ParentDepartmentId": "6"
                }
            ],
            "Total": 2
        }
    }
}
```

