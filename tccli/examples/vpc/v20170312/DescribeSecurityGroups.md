**Example 1: Querying security groups**



Input: 

```
tccli vpc DescribeSecurityGroups --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Name project-id \
    --Filters.0.Values 0 \
    --Filters.1.Name security-group-name \
    --Filters.1.Values TestGroup
```

Output: 
```
{
    "Response": {
        "SecurityGroupSet": [
            {
                "SecurityGroupId": "sg-05bb4upy",
                "SecurityGroupName": "TestGroup",
                "SecurityGroupDesc": "test-group-desc",
                "ProjectId": "0",
                "CreateTime": "2017-04-18 21:02:30"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

**Example 2: Querying security groups bound with the tag**

Queries using tag:tag-key.

Input: 

```
tccli vpc DescribeSecurityGroups --cli-unfold-argument  \
    --Filters.0.Name tag:Version \
    --Filters.0.Values TEST
```

Output: 
```
{
    "Response": {
        "SecurityGroupSet": [
            {
                "SecurityGroupId": "sg-2got2lcz",
                "SecurityGroupName": "test",
                "SecurityGroupDesc": "Exposing all ports to the Internet and private network may introduce security risks",
                "ProjectId": "0",
                "IsDefault": false,
                "CreatedTime": "2019-07-23 12:32:24",
                "TagSet": [
                    {
                        "Key": "Tag key",
                        "Value": "Tag value"
                    },
                    {
                        "Key": "Version",
                        "Value": "TEST"
                    },
                    {
                        "Key": "Version",
                        "Value": "DEV"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "85cda7d1-6608-4eca-8d02-19937c12dd84"
    }
}
```

