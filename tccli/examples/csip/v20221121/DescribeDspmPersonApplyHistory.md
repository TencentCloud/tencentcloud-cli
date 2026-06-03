**Example 1: 查询Dspm访客申请记录**



Input: 

```
tccli csip DescribeDspmPersonApplyHistory --cli-unfold-argument  \
    --Subject 100000 \
    --AssetId cdb-c2thbt00
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ApplySet": [],
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

