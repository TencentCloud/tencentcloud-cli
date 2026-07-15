**Example 1: 查询监听器绑定证书列表**



Input: 

```
tccli alb DescribeListenerCertificates --cli-unfold-argument  \
    --CertificateType SVR \
    --ListenerId lst-d9p3k7wa \
    --LoadBalancerId alb-f8q2xk9m \
    --MaxResults 20
```

Output: 
```
{
    "Response": {
        "Certificates": [
            {
                "CertificateId": "Fm8Wp7x8",
                "CertificateType": "SVR",
                "AssociatedTime": "2024-06-12T10:34:56Z",
                "IsDefault": true,
                "Status": "Associated"
            }
        ],
        "MaxResults": 20,
        "NextToken": "2c44874464923a9f",
        "TotalCount": 200,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

