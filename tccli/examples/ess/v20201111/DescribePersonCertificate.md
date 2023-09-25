**Example 1: 查询个人自动签证书**

1.张三已开通自动签署服务
2.查询个人用户张三的自动签证书信息

Input: 

```
tccli ess DescribePersonCertificate --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 张三 \
    --UserInfo.IdCardNumber 37000019890303000X \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN
```

Output: 
```
{
    "Response": {
        "Cert": "MIIFvDCCBKSgAwIBAgIKLEAAAAAAAeG/JDANBgkqhkiG9w0Sz+zaDmLEK2odEmlMwKdeNd0vRb47sp3jkUSs46FL7rblJ4puClqKF4FxkDMpgAH7Gt6wwaeejbj+r+EVSKjV2nkBAA6rgMZuY24vY3BzMBUGCiqBHIbvMgIBAR4EBwwFOTYwMDMwDQYJKoZIhvcNAQELBQADggEBAKuOn//LFHqcu2ec2VyNvgizNx5J1CuDjR4wZkTJTvy/ydNQnQpVZRKAfNQ1gz+QerNqrSVH//3tGk42rQGumDAv2vTGBU7lrs4/QCPSvBpQGgDYXuKU5LyNh80eVy7LyurRTlQT+t22DPjN5gjuk4UE5q8Hv5SO7q6mowHFG3+HLsi1K1TMrN151Ebi4TUzK0keiGYBqiK6/h6q4xSyTyPmy+SiNgmXiRYkWPdBJBckgDqw/7/qEXp1N9fswbrWYA/W5P6DjYDZDmApRsQkAYsBdxrAngTl3tOkZTFX8oFu2Hv+8oW5Y0jYLnGQ2NFl901d6cPnzcAXMs5nQhbY690=",
        "RequestId": "s169529xxxxx93567314"
    }
}
```

**Example 2: 查询个人自动签证书-用户未开通自动签**

1.张三没有开通自动签署服务
2.查询个人用户张三的自动签证书信息

Input: 

```
tccli ess DescribePersonCertificate --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 张三 \
    --UserInfo.IdCardNumber 37000019890303000X \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "个人未开通自动签"
        },
        "RequestId": "s169529xxxxx135883849"
    }
}
```

