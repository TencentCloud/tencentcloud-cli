**Example 1: 新增加速域名**

新增加速域名

Input: 

```
tccli cdn AddCdnDomain --cli-unfold-argument  \
    --Origin.OriginType ip \
    --Origin.Origins 1.1.1.1 \
    --ProjectId 0 \
    --Domain www.test.com \
    --ServiceType web \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "RequestId": "a4ac88a3-a159-47ac-9b87-19185d7deb09"
    }
}
```

