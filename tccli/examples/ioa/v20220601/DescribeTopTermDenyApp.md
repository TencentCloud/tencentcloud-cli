**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeTopTermDenyApp --cli-unfold-argument  \
    --StartTime 1683703604000 \
    --EndTime 1685431604000 \
    --From 0 \
    --Size 2 \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Count": 5,
                    "ProcessName": "chrome.exe",
                    "ProcessPath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "Rank": 1
                },
                {
                    "Count": 1,
                    "ProcessName": "11999.exe",
                    "ProcessPath": "C:xxxyy",
                    "Rank": 2
                }
            ],
            "Total": 7
        },
        "RequestId": "3bf061d1-4982-4597-94fc-2d9974d785e8"
    }
}
```

**Example 2: DescribeTopTermDenyApp**

DescribeTopTermDenyApp

Input: 

```
tccli ioa DescribeTopTermDenyApp --cli-unfold-argument  \
    --StartTime 1 \
    --EndTime 1 \
    --Department 1 \
    --From 1 \
    --Size 1 \
    --Sort 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "648753d9-c688-4b1c-987b-4725a6e79e79"
    }
}
```

