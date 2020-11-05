**Example 1: Adding an acceleration domain name**



Input: 

```
tccli cdn AddCdnDomain --cli-unfold-argument  \
    --Domain www.test.com\
    --ServiceType web\
    --ProjectId 0\
    --Area mainland\
    --Origin.Origins 1.1.1.1\
    --Origin.OriginType ip
```

Output: 
```
{
    "Response": {
        "RequestId": "a4ac88a3-a159-47ac-9b87-19185d7deb09"
    }
}
```

