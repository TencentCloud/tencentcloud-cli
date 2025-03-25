**Example 1:  查询权限配置部署列表**

 查询权限配置部署列表

Input: 

```
tccli organization ListRoleConfigurationProvisionings --cli-unfold-argument  \
    --ZoneId z-d8wj \
    --RoleConfigurationId up-dnsisns*** \
    --MaxResults 20 \
    --NextToken sgt**** \
    --TargetType MemberUin \
    --TargetUin 1000329122 \
    --DeploymentStatus DeployedRequired \
    --Filter conf1
```

Output: 
```
{
    "Response": {
        "NextToken": "",
        "TotalCounts": 30,
        "MaxResults": 10,
        "IsTruncated": true,
        "RoleConfigurationProvisionings": [
            {
                "DeploymentStatus": "DeployedRequired",
                "RoleConfigurationId": "rc-sjwiwm2ww**",
                "RoleConfigurationName": "conf1",
                "TargetUin": 10003292021,
                "TargetName": "user1",
                "TargetType": "MemberUin",
                "CreateTime": "2024-01-01 12:12:12",
                "UpdateTime": "2024-01-01 12:12:12"
            }
        ],
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

