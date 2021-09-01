**Example 1: 获取策略版本列表**

获取一个策略的版本列表

Input: 

```
tccli cam ListPolicyVersions --cli-unfold-argument  \
    --PolicyId 17698703
```

Output: 
```
{
    "Response": {
        "Versions": [
            {
                "VersionId": 2,
                "CreateDate": "2019-08-09T10:31:47Z",
                "IsDefaultVersion": 1
            },
            {
                "VersionId": 3,
                "CreateDate": "2019-08-09T10:31:47Z",
                "IsDefaultVersion": 0
            }
        ],
        "RequestId": "13567bf0-a52b-49af-a3ce-ea934ef33c57"
    }
}
```

