**Example 1: 批量查询DataSight控制台实例列表**

批量查询DataSight控制台实例列表

Input: 

```
tccli cls DescribeConsoles --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Consoles": [
            {
                "AccessMode": [
                    "internal"
                ],
                "Accounts": null,
                "AnonymousLogin": null,
                "AuthRoles": [
                    {
                        "RoleName": "rolename",
                        "SecretId": "secretid",
                        "SecretKey": null
                    }
                ],
                "ConsoleId": "clsconsole-xxxxxxxx",
                "DomainPrefix": "datasight",
                "IntranetRegion": "ap-guangzhou",
                "IntranetType": 0,
                "LoginMode": 2,
                "SubnetId": "subnet-xxxxxxxx",
                "VpcId": "vpc-xxxxxxxx"
            }
        ],
        "RequestId": "xxxxxxxx"
    }
}
```

