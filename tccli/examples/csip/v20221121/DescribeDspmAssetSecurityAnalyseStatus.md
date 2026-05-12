**Example 1: 查询Dspm资产安全分析状态**



Input: 

```
tccli csip DescribeDspmAssetSecurityAnalyseStatus --cli-unfold-argument  \
    --MemberId mem-6wfo0fzks3 \
    --Filter.Limit 100
```

Output: 
```
{
    "Response": {
        "AssetSet": [],
        "TotalCount": 0,
        "RequestId": "af6e2ac5-e336-42be-b994-c2225b411397"
    }
}
```

