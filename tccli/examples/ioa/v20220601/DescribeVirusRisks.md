**Example 1: 示例1**



Input: 

```
tccli ioa DescribeVirusRisks --cli-unfold-argument  \
    --Mid F1AFD85EC54480393C546B99C7CD014963761895
```

Output: 
```
{
    "Response": {
        "RequestId": "0a04f598-6b6c-4336-9479-3704c057b56a",
        "Data": {
            "Paging": {
                "PageSize": 0,
                "PageNum": 0,
                "PageCount": 0,
                "Total": 0
            },
            "Items": []
        }
    }
}
```

**Example 2: DescribeVirusRisks**

DescribeVirusRisks

Input: 

```
tccli ioa DescribeVirusRisks --cli-unfold-argument  \
    --Mid 123456 \
    --Condition.PageSize 10 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "6ad92e62-b40c-4d78-b0db-1682632bcd16"
    }
}
```

