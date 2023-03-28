**Example 1: 示例-主代子绑定角色**

示例-主代子绑定角色

Input: 

```
tccli ess CreateIntegrationUserRoles --cli-unfold-argument  \
    --Agent.ProxyOrganizationId yDwcwUUgyg3ku4dcUnb2eQRA5tb3wCvJ \
    --UserIds yDwcwUUgyg3kuuemUnb2eQS1BsaTeVDP \
    --RoleIds 6fad1903eea5074122d6921046819037 \
    --Operator.UserId yDwnHUUgygksdjwxUuMR3gQvehewF4C5 \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.Channel YUFU
```

Output: 
```
{
    "Response": {
        "FailedCreateRoleData": [],
        "RequestId": "s1679478914712921175"
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
    --Operator.UserId y**********************************s \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.Channel YUFU
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

