**Example 1: 以产品维度获取企业财务信息**

以产品维度获取企业财务信息

Input: 

```
tccli organization DescribeOrganizationFinancialByProduct --cli-unfold-argument  \
    --Month 2021-04
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ProductCode": "e-cdb",
                "ProductName": "mysql",
                "TotalCost": 33.23,
                "Ratio": "70"
            },
            {
                "ProductCode": "e-cos",
                "ProductName": "cos对象存储",
                "TotalCost": 10.12,
                "Ratio": "30"
            }
        ],
        "RequestId": "d581d282-3acf-496f-b7ba-0fe640648183",
        "TotalCost": 1002.1,
        "Total": 2
    }
}
```

