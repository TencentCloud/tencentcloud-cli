**Example 1: 获取信审结果**



Input: 

```
tccli cr DescribeCreditResult --cli-unfold-argument  \
    --Module Credit \
    --Operation Get \
    --InstId 123 \
    --ProductId 123 \
    --CaseId 123 \
    --RequestDate YYYY-MM-DD
```

Output: 
```
{
    "Response": {}
}
```

