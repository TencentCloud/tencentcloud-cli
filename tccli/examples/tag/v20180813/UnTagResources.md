**Example 1: 为资源解绑标签**



Input: 

```
tccli tag UnTagResources --cli-unfold-argument  \
    --ResourceList qcs::cvm:ap-beijing:uin/10000055****:instance/**** qcs::cvm:ap-beijing:uin/10000055****:instance/**** \
    --TagKeys RWFGaltFlR LbDKGjeagV
```

Output: 
```
{
    "Response": {
        "FailedResources": [],
        "RequestId": "cbc7b26c-3fff-4a3c-82f0-c6ebc2ff31e3"
    }
}
```

