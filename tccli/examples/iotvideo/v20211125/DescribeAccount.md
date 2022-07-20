**Example 1: 拉取云存的账号信息**



Input: 

```
tccli iotvideo DescribeAccount --cli-unfold-argument  \
    --AccountType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "124aa145i30913",
        "Uin": "9945855",
        "BillType": 1,
        "BillMode": 2
    }
}
```

