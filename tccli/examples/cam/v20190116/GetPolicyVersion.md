**Example 1: 查询策略版本详情**

查询一个策略版本详情

Input: 

```
tccli cam GetPolicyVersion --cli-unfold-argument  \
    --PolicyId 17698703 \
    --VersionId 2
```

Output: 
```
{
    "Response": {
        "PolicyVersion": {
            "VersionId": 2,
            "CreateDate": "2019-08-09T10:31:47Z",
            "IsDefaultVersion": 1,
            "Document": "{\"version\":\"2.0\",\"statement\":[{\"effect\":\"allow\",\"action\":[\"name\\/cos:*\"],\"resource\":[\"*\"]}]}"
        },
        "RequestId": "8a0668c1-2d9b-40a5-acc6-151ea3c844e7"
    }
}
```

