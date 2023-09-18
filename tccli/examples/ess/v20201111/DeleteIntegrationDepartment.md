**Example 1: 删除部门**

删除部门，并设置了交接部门。该部门的数据将被交接至对应部门下。

Input: 

```
tccli ess DeleteIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc********QZDRuD \
    --DeptId yDwgIUUckp1g********E8xOm12b9 \
    --ReceiveDeptId yDRIoUUgyg********SXSVVSJ1z
```

Output: 
```
{
    "Response": {
        "RequestId": "f94cxxxx-xxxx-xxxx-xxxx-xxxxxxxxb420"
    }
}
```

**Example 2: 错误示例-未授权操作**

调用此接口前，需确保用户拥有“编辑组织架构”权限。否则接口将返回错误信息。

Input: 

```
tccli ess DeleteIntegrationDepartment --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc********QZDRuE \
    --DeptId yDwgIUUckp1g********E8xOm12b9 \
    --ReceiveDeptId yDRIoUUgyg********SXSVVSJ1z
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作（编辑组织架构）"
        },
        "RequestId": "f94cxxxx-xxxx-xxxx-xxxx-xxxxxxxxb420"
    }
}
```

