**Example 1: 批量更新API超时**



Input: 

```
tccli tsf UpdateApiTimeouts --cli-unfold-argument  \
    --ApiIds api-tnvxy4ta \
    --UsableStatus enabled \
    --Timeout 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "30356074-f0ce-46a3-86fd-30da5fcf336e",
        "Result": true
    }
}
```

