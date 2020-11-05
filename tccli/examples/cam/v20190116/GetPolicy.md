**Example 1: Viewing policy details**



Input: 

```
tccli cam GetPolicy --cli-unfold-argument  \
    --PolicyId 17698703
```

Output: 
```
{
    "Response": {
        "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":[\"name\\/cos:*\"],\"resource\":[\"*\"]}]}",
        "UpdateTime": "2019-04-29 21:28:32",
        "AddTime": "2019-04-29 21:18:40",
        "PolicyName": "test-2019-04-29",
        "Description": "Test policy",
        "Type": 1,
        "RequestId": "845b309d-e531-402d-a4f6-ec124f06738b",
        "PresetAlias": "Remarks",
        "IsServiceLinkedRolePolicy": 0
    }
}
```

