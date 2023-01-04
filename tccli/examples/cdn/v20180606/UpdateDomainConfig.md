**Example 1: 更新域名配置**



Input: 

```
tccli cdn UpdateDomainConfig --cli-unfold-argument  \
    --ProjectId 0 \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "23cd4005-496f-4bc4-87d8-ab348d5b0c17"
    }
}
```

**Example 2: bennyddeng-test**



Input: 

```
tccli cdn UpdateDomainConfig --cli-unfold-argument  \
    --Domain test02.lukachen.work \
    --HttpsBilling.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "283d5206-8768-4322-8a68-8c1d09afcdff"
    }
}
```

