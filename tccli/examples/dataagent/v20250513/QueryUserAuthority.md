**Example 1: 示例**

示例

Input: 

```
tccli dataagent QueryUserAuthority --cli-unfold-argument  \
    --InstanceId dataagent-G5XTaxnz \
    --Module knowledge \
    --ObjectId klbase-uKGsu3qP6p
```

Output: 
```
{
    "Response": {
        "RequestId": "dfd48354-970d-4368-9c6d-536579b53a86",
        "ModelUserAuthority": {
            "Module": "knowledge",
            "InstanceId": "dataagent-G5XTaxnz",
            "CreatorUin": "100021289371",
            "ObjectId": "klbase-uKGsu3qP6p",
            "UseScope": 0,
            "AuthorityUins": [],
            "CreateTime": "2025-12-30T17:58:25+08:00",
            "UpdateTime": "2025-12-30T18:05:47+08:00"
        }
    }
}
```

