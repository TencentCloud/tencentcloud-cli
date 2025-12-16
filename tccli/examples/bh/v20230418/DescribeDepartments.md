**Example 1: 查询部门信息**

查询部门信息

Input: 

```
tccli bh DescribeDepartments --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082",
        "Departments": {
            "DepartmentSet": [
                {
                    "Managers": [
                        "bh_admin_user"
                    ],
                    "Id": "1",
                    "Name": "运维部"
                }
            ],
            "Enabled": true,
            "RootManager": true
        }
    }
}
```

