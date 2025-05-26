**Example 1: 删除用户组**



Input: 

```
tccli emr DeleteGroupsSTD --cli-unfold-argument  \
    --InstanceId emr-o88f3whr \
    --GroupNames group1 group2
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Item": "group1",
                "Reason": "",
                "Result": true
            },
            {
                "Item": "group2",
                "Reason": "Group group2 not found or being processed",
                "Result": false
            }
        ],
        "RequestId": "24b928fe-29f4-4c15-8a4c-700eb86c713a"
    }
}
```

