**Example 1: 增加用户组**



Input: 

```
tccli emr CreateGroupsSTD --cli-unfold-argument  \
    --InstanceId emr-mzkssfla \
    --Groups.0.GroupName testgroup1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Item": "testgroup1",
                "Reason": "",
                "Result": true
            }
        ],
        "RequestId": "ecb47f14-b4a5-4a7b-bf3e-0664606778af"
    }
}
```

