**Example 1: 示例1**

通过子企业影子账号查询主企业员工账号

Input: 

```
tccli ess DescribeIntegrationMainOrganizationUser --cli-unfold-argument  \
    --Operator.UserId y********************F
```

Output: 
```
{
    "Response": {
        "IntegrationMainOrganizationUser": {
            "MainOrganizationId": "y**************************w",
            "MainUserId": "y************************2",
            "UserName": "胡*"
        },
        "RequestId": "s1673xxxxx880372"
    }
}
```

