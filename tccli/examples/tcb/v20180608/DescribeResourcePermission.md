**Example 1: 批量查询SQL型数据库表的基础权限**

查询SQL型数据库表users的基础权限

Input: 

```
tccli tcb DescribeResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType table \
    --Resources users
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionList": [
                {
                    "Permission": "ADMINWRITE",
                    "Resource": "users",
                    "ResourceType": "table"
                }
            ],
            "TotalCount": 2
        },
        "RequestId": "b71b3f05-0735-4320-9ef2-40b888bc42d0"
    }
}
```

**Example 2: 批量查询云存储桶的基础权限**

查询桶的基础权限

Input: 

```
tccli tcb DescribeResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf09******** \
    --ResourceType storage \
    --Resources us***
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionList": [
                {
                    "Permission": "READONLY",
                    "Resource": "us***",
                    "ResourceType": "storage",
                    "SecurityRule": ""
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "76cee3db-ce4e-4428-9de0-04e1d5d6c1b8"
    }
}
```

**Example 3: 批量查询文档型数据库表的基础权限**

查询文档型数据库表testte的基础权限

Input: 

```
tccli tcb DescribeResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType collection \
    --Resources testte
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionList": [
                {
                    "Permission": "READONLY",
                    "Resource": "testte",
                    "ResourceType": "collection",
                    "SecurityRule": ""
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "68c382a1-fb7a-4e43-b0f4-7f153c9c9bf2"
    }
}
```

**Example 4: 查询云函数的安全规则**

查询云函数的安全规则

Input: 

```
tccli tcb DescribeResourcePermission --cli-unfold-argument  \
    --EnvId **test-1gahsf0********* \
    --ResourceType function
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionList": [
                {
                    "Permission": "CUSTOM",
                    "Resource": "",
                    "ResourceType": "function",
                    "SecurityRule": "{\n    \"*\": {\n        \"invoke\": true    }\n}"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "8b4c9ee3-152e-44a5-a97a-5afff7571a22"
    }
}
```

