**Example 1: 增加用户组**



Input: 

```
tccli emr CreateGroupsSTD --cli-unfold-argument  \
    --InstanceId emr-o88f3whr \
    --Groups.0.GroupName group4 \
    --Groups.0.Description ceshi
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Item": "group4",
                "Reason": "",
                "Result": true
            }
        ],
        "RequestId": "ceff5822-18bb-43d7-8c63-199597aa50de"
    }
}
```

