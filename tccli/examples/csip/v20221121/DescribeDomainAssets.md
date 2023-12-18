**Example 1: 接口示例**

接口示例

Input: 

```
tccli csip DescribeDomainAssets --cli-unfold-argument  \
    --MemberId abc \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "AssetLocationList": [],
        "Data": null,
        "DefenseStatusList": [],
        "RegionList": [],
        "RequestId": "16cd9855-3a4c-4a65-a7f7-1ac66472d103",
        "SourceTypeList": [],
        "Total": 0
    }
}
```

