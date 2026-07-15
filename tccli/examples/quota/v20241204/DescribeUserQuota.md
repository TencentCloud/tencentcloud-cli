**Example 1: 示例1**



Input: 

```
tccli quota DescribeUserQuota --cli-unfold-argument  \
    --ProductName Your Product Name
```

Output: 
```
{
    "Response": {
        "ProductName": "Your Product Name",
        "QuotaDescription": "quota desc",
        "QuotaId": 8888,
        "QuotaName": "quota name",
        "QuotaUnit": "quota unit",
        "RequestId": "f089d37f-3d61-46fd-9b84-xxxxxx",
        "TotalQuota": 15,
        "TotalUsage": 0
    }
}
```

