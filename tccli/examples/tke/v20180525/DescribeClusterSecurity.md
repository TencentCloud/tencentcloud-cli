**Example 1: Querying key information of a cluster**

Queries the key information of a cluster

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

