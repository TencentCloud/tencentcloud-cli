**Example 1: 更新资产搜索视图**



Input: 

```
tccli csip ModifyAssetFilterView --cli-unfold-argument  \
    --ViewID 6 \
    --MemberId mem-0*c*10*2f*a**aee \
    --Filters.0.Name InstanceID \
    --Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "Message": "Success",
        "RequestId": "b0f9674f-b526-4a06-9010-dd352ebd23b5"
    }
}
```

