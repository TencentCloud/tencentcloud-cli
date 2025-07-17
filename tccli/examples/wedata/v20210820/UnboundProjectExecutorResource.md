**Example 1: ewe**

32

Input: 

```
tccli wedata UnboundProjectExecutorResource --cli-unfold-argument  \
    --ExecutorGroupId 0 \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "ad1f4c7c-d84a-44ce-a2a9-308f236c0ed1"
    }
}
```

**Example 2: 解绑项目**

解绑多个

Input: 

```
tccli wedata UnboundProjectExecutorResource --cli-unfold-argument  \
    --ExecutorGroupId 20220706111614878854 \
    --ProjectId 1091118890164248576 \
    --ExecutorResourcePackageIds 20220706111615206649
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "a6bb0018-c093-4fb8-8984-1b7c212f47c5"
    }
}
```

