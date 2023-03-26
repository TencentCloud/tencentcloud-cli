**Example 1: 查询COS桶列表**



Input: 

```
tccli tiw DescribeAPIService --cli-unfold-argument  \
    --Service cos:GetService \
    --Data 
```

Output: 
```
{
    "Response": {
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351",
        "ResponseData": "{\"Bucket\": \"test\"}"
    }
}
```

