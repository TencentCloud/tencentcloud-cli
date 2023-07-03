**Example 1: 查询子客uin列表**

查询子客uin列表

Input: 

```
tccli intlpartnersmgt DescribeCustomerUin --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CustomerUin": "123"
            }
        ],
        "Total": "123",
        "RequestId": "abc"
    }
}
```

