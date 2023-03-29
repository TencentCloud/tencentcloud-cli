**Example 1: 开通后付费资源**

开通后付费资源

Input: 

```
tccli tcb CreatePostpayPackage --cli-unfold-argument  \
    --EnvId cdnheader-v2a \
    --FreeQuota basic
```

Output: 
```
{
    "Response": {
        "EnvId": "cdnheader-v2a",
        "RequestId": "52537e93-2a50-4269-a638-e03e6bb6426e",
        "TranId": "20200603119423"
    }
}
```

