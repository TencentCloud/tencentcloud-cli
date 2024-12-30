**Example 1: 根据ccn-ids过滤查询**

根据ccn-ids过滤查询

Input: 

```
tccli vpc DescribeTenantCcns --cli-unfold-argument  \
    --Filters.0.Values ccn-gyt67ffz \
    --Filters.0.Name ccn-ids
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-gyt67ffz"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ff8a76ff-8900-4169-b126-ff59fdb39b6c"
    }
}
```

**Example 2: 根据user-account-id过滤查询**

根据user-account-id过滤查询

Input: 

```
tccli vpc DescribeTenantCcns --cli-unfold-argument  \
    --Filters.0.Values 1742152960 \
    --Filters.0.Name user-account-id
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-kwgk02zl"
            },
            {
                "CcnId": "ccn-gyt67ffz"
            },
            {
                "CcnId": "ccn-e7wopzfz"
            }
        ],
        "TotalCount": 3,
        "RequestId": "6c72d2a1-b60c-464e-b782-ca6efe7c1dd6"
    }
}
```

**Example 3: 根据is-security-lock过滤查询**

根据is-security-lock过滤查询

Input: 

```
tccli vpc DescribeTenantCcns --cli-unfold-argument  \
    --Filters.0.Values false \
    --Filters.0.Name is-security-lock
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-d0s0mkw1"
            },
            {
                "CcnId": "ccn-kwgk02zl"
            },
            {
                "CcnId": "ccn-gyt67ffz"
            },
            {
                "CcnId": "ccn-e7wopzfz"
            }
        ],
        "TotalCount": 5,
        "RequestId": "495efea0-0073-451c-a577-77a23626432c"
    }
}
```

