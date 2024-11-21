**Example 1: 删除公网IP/域名**

删除公网IP/域名

Input: 

```
tccli csip DeleteDomainAndIp --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Content.0.Asset 172.**.**.1 \
    --RetainPath 0 \
    --IgnoreAsset 0 \
    --Tags.0.TagKey foo \
    --Tags.0.TagValue foo \
    --Type CLB
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "7cf2ba3d-87ad-4691-a374-fd92ec11d9c8"
    }
}
```

