**Example 1: 按月维度获取企业财务趋势**

按月维度获取企业财务趋势

Input: 

```
tccli organization DescribeOrganizationFinancialByMonth --cli-unfold-argument  \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Id": 7,
                "Month": "2021-06",
                "TotalCost": 10232.1
            },
            {
                "Id": 5,
                "Month": "2021-05",
                "TotalCost": 1002.1
            },
            {
                "Id": 3,
                "Month": "2021-04",
                "TotalCost": 1002.1
            }
        ],
        "RequestId": "89c5de68-2306-48df-9e81-ad2953447e7a"
    }
}
```

