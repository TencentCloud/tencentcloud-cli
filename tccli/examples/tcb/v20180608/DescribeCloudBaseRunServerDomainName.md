**Example 1: DescribeCloudBaseRunServerDomainName**



Input: 

```
tccli tcb DescribeCloudBaseRunServerDomainName --cli-unfold-argument  \
    --ServerName server \
    --UserEnvId env-sdff \
    --UserUin 1242344 \
    --ExternalId sdff
```

Output: 
```
{
    "Response": {
        "RequestId": "sdfsfsdf",
        "DomainName": "",
        "InternalDomain": "",
        "PublicDomain": ""
    }
}
```

