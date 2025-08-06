**Example 1: 更新访问凭证**

轮转替换访问凭证，需要传入旧访问凭证

Input: 

```
tccli tcr UpdateApplicationTokenPersonal --cli-unfold-argument  \
    --OldApplicationToken {ApplicationToken:mock00000000}
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApplicationToken": "{ApplicationToken:mock66666666}"
        },
        "RequestId": "57d4103b-6082-4589-9902-6076386ee07b"
    }
}
```

**Example 2: 更新只读访问凭证**

轮转替换只读访问凭证，需要传入旧只读访问凭证

Input: 

```
tccli tcr UpdateApplicationTokenPersonal --cli-unfold-argument  \
    --OldApplicationToken {RoToken:mock00000000} \
    --Readonly True
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApplicationToken": "{RoToken:mock66666666}"
        },
        "RequestId": "faa9bec3-3cf4-4ea9-83fc-d5153e5ddb14"
    }
}
```

