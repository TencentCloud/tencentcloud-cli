**Example 1: 解绑不区分地域资源的历史标签（绑定标签的资源带有地域）**



Input: 

```
tccli tag DeleteNoDistinctRegionResourceTag --cli-unfold-argument  \
    --TagKey testKey \
    --Resource qcs::waf:ap-guangzhou:uin/100000005307:waf/waf_001
```

Output: 
```
{
    "Response": {
        "RequestId": "16823c00-cbad-4e0c-8b8d-eececc59bb38"
    }
}
```

