**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeTopTermDenyClient --cli-unfold-argument  \
    --StartTime 1683703604000 \
    --EndTime 1685431604000 \
    --From 0 \
    --Size 10 \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Account": "",
                    "AccountName": "",
                    "Count": 10,
                    "GroupName": "未分组终端",
                    "IpPort": "154.8.246.196",
                    "LocalIpList": "",
                    "Mac": "08:00:27:30:A2:52",
                    "Name": "DESKTOP-QMN3FBP",
                    "Rank": 1,
                    "User": "bernard"
                },
                {
                    "Account": "",
                    "AccountName": "",
                    "Count": 1,
                    "GroupName": "",
                    "IpPort": "154.8.246.196",
                    "LocalIpList": "",
                    "Mac": "",
                    "Name": "",
                    "Rank": 2,
                    "User": ""
                }
            ],
            "Total": 2
        },
        "RequestId": "b741664c-b335-4ee0-8560-fff832702d7d"
    }
}
```

**Example 2: DescribeTopTermDenyClient**

DescribeTopTermDenyClient

Input: 

```
tccli ioa DescribeTopTermDenyClient --cli-unfold-argument  \
    --StartTime 1 \
    --EndTime 1 \
    --Department 1 \
    --From 132 \
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
        "RequestId": "8e98f2dc-599e-4f6a-9691-b7fbc7afc270"
    }
}
```

