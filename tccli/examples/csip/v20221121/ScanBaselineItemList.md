**Example 1: 扫描检测项风险**

扫描检测项风险

Input: 

```
tccli csip ScanBaselineItemList --cli-unfold-argument  \
    --PolicyType SELF \
    --PolicyID 2 \
    --CategoryID 209 \
    --ParentCategoryID 2 \
    --ItemIDList 2123 \
    --MemberId mem-************95752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "1f99c099-c4f5-442c-9620-d02f995199c6"
    }
}
```

