**Example 1: 添加资产**



Input: 

```
tccli csip CreateDomainAndIp --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Content 127.0.0.1 \
    --Tags.0.TagKey sec \
    --Tags.0.TagValue sec
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "RequestId": "7cf2ba3d-87ad-4691-a374-fd92ec11d9c8"
    }
}
```

