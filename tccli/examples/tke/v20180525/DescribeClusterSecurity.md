**Example 1: 集群的密钥信息**

集群的密钥信息

Input: 

```
tccli tke DescribeClusterSecurity --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "UserName": "xxxxx",
        "CertificationAuthority": "xxxxxx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

