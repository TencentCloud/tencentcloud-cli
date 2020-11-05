**Example 1: Getting a list of policy versions**

This example shows you how to get the list of policy versions.

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

