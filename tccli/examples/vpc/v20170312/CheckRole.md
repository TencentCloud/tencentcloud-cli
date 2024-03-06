**Example 1: 查询用户角色是否存在**

查询用户角色是否存在

Input: 

```
tccli vpc CheckRole --cli-unfold-argument  \
    --RoleName VPC_QCSLinkedRoleInEipTat
```

Output: 
```
{
    "Response": {
        "RoleName": "VPC_QCSLinkedRoleInEipTat",
        "RoleExist": true,
        "RequestId": "0fbc7c1c-d78b-47b7-ab7a-7893bf1d4a95"
    }
}
```

