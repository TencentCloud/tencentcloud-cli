**Example 1: 创建资产搜索视图**



Input: 

```
tccli csip CreateAssetFilterView --cli-unfold-argument  \
    --ViewName 爱迪生 \
    --MemberId mem-0acb*0*2f9*4daee \
    --Filters.0.Name AssetName \
    --Filters.0.Values 爱迪生
```

Output: 
```
{
    "Response": {
        "Message": "Success",
        "RequestId": "f7c72f31-f220-4866-b714-7e3e3842d913"
    }
}
```

