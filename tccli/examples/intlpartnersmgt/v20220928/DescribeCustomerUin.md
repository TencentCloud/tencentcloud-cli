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
                "CustomerUin": "200000000000"
            }
        ],
        "Total": "1",
        "RequestId": "b8fccb85-c0d2-46b7-a5ea-1d24fbd3b38c"
    }
}
```

