**Example 1: 删除平台域名**



Input: 

```
tccli tcb DeletePlatformHTTPServiceRoute --cli-unfold-argument  \
    --PlatformId pf-t960szfwv1cs \
    --Domain *.rgw.***************.cn \
    --Paths /
```

Output: 
```
{
    "Response": {
        "RequestId": "f8aec3a6-eae0-4fee-bdd3-0fdbcf7ed168"
    }
}
```

