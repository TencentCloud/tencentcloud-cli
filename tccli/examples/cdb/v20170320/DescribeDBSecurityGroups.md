**Example 1: Querying the security group information of instance**



Input: 

```
tccli cdb DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId cdb-eb2w7dto
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Groups": [
            {
                "Outbound": [],
                "SecurityGroupName": "CDB",
                "Inbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-ajr1jzgj",
                "SecurityGroupRemark": "",
                "CreateTime": "2017-04-13 15:00:06"
            }
        ]
    }
}
```

