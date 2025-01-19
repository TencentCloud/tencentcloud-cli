**Example 1: DescribeCustomerBillDownloadUrl-1**

经销商下载直接子客L2资源账单

Input: 

```
tccli intlpartnersmgt DescribeCustomerBillDownloadUrl --cli-unfold-argument  \
    --Month 2024-12 \
    --FileType billResource \
    --CustomerUinType Customer \
    --CustomerUin 800000425835
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://partner-bill-xxxx.cos.ap-singapore.myqcloud.com/L2-bill_by_Instance-800000425835-202412-xx-test.csv",
        "Ready": 1,
        "RequestId": "fa772ee3-e610-4e5b-905e-35c92a13e052"
    }
}
```

**Example 2: DescribeCustomerBillDownloadUrl-2**

经销商获取间接子客L3账单详情链接

Input: 

```
tccli intlpartnersmgt DescribeCustomerBillDownloadUrl --cli-unfold-argument  \
    --Month 2024-12 \
    --FileType billDetail \
    --CustomerUinType ResellerCustomer \
    --CustomerUin 800001608331
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://partner-bill-xxx.cos.ap-singapore.myqcloud.com/L3-bill_details-800001608331-202412-xxx-test.csv",
        "Ready": 1,
        "RequestId": "b93fad4a-1ef8-4011-a93b-bf8b6b5ee3ee"
    }
}
```

**Example 3: DescribeCustomerBillDownloadUrl-3**

经销商获取全部子客L2资源账单包（已出账）

Input: 

```
tccli intlpartnersmgt DescribeCustomerBillDownloadUrl --cli-unfold-argument  \
    --Month 2024-11 \
    --FileType billResourcePack \
    --CustomerUinType Customer
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://partner-bill-xxx.cos.ap-singapore.myqcloud.com/%2Fmnt/bill/en/L2-bill_by_Instance-800000950266-AllCustomersBills-202411-xxx-test.zip",
        "Ready": 1,
        "RequestId": "0aa8fe2c-5221-4d94-b481-3f329c89b25a"
    }
}
```

**Example 4: DescribeCustomerBillDownloadUrl-4**

经销商获取全部间接子客L3账单详情账单包（已出账）

Input: 

```
tccli intlpartnersmgt DescribeCustomerBillDownloadUrl --cli-unfold-argument  \
    --Month 2024-11 \
    --FileType billDetailPack \
    --CustomerUinType ResellerCustomer
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://partner-bill-xxxx.cos.ap-singapore.myqcloud.com/%2Fmnt/bill/en/L3-bill_details-800000950266-AllResellersBills-202411-xxxx-test.zip",
        "Ready": 1,
        "RequestId": "fb76a1cd-7b8e-435a-909e-3f8ec3b91c9a"
    }
}
```

