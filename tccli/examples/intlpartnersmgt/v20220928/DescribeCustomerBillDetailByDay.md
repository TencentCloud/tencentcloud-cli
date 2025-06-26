**Example 1: 经销商查询子客日账单消费**



Input: 

```
tccli intlpartnersmgt DescribeCustomerBillDetailByDay --cli-unfold-argument  \
    --CustomerUin 123123123 \
    --Date 2025-01-01
```

Output: 
```
{
    "Response": {
        "RequestId": "asdfasd-asdasdasd-123123asdas",
        "TotalCost": "123.12312312"
    }
}
```

