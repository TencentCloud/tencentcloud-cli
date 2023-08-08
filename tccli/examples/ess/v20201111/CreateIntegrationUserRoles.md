**Example 1: 示例-主代子绑定角色**

示例-主代子绑定角色

Input: 

```
tccli ess CreateIntegrationUserRoles --cli-unfold-argument  \
    --Agent.ProxyOrganizationId yDwcwUUg*****b2eQRA5tb3wCvJ \
    --UserIds yDwcwUUgyg3****2eQS1BsaTeVDP \
    --RoleIds 6fad1903****6921046819037 \
    --Operator.UserId yDwnHUU****MR3gQvehewF4C5
```

Output: 
```
{
    "Response": {
        "FailedCreateRoleData": [],
        "RequestId": "s1679*****21175"
    }
}
```

**Example 2: 示例-普通企业绑定角色**

示例-普通企业绑定角色

Input: 

```
tccli ess CreateIntegrationUserRoles --cli-unfold-argument  \
    --UserIds y**************************************************s y**************************************************e \
    --RoleIds 0************************************************e f*************************************************b \
    --Operator.UserId y**********************************s
```

Output: 
```
{
    "Response": {
        "FailedCreateRoleData": [
            {
                "RoleIds": [
                    "**************************************************",
                    "**************************************************"
                ],
                "UserId": "*******************************************"
            }
        ],
        "RequestId": "s******************"
    }
}
```

