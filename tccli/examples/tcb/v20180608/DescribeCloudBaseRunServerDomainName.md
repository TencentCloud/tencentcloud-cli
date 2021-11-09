**Example 1: DescribeCloudBaseRunServerDomainName**



Input: 

```
tccli tcb DescribeCloudBaseRunServerDomainName --cli-unfold-argument  \
    --ServerName xxxxxxx \
    --UserEnvId xxxxx \
    --UserUin xxxxxx \
    --ExternalId xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DomainName": "xxxxxx",
        "InternalDomain": "xxxxxx",
        "PublicDomain": "xxxxxx"
    }
}
```

