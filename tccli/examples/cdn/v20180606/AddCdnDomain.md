**Example 1: 新增加速域名**



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

**Example 2: bennyddeng-test**



Input: 

```
tccli cdn AddCdnDomain --cli-unfold-argument  \
    --Origin.OriginPullProtocol http \
    --Origin.ServerName test04.lukachen.work \
    --Origin.OriginType domain \
    --Origin.Origins www.baidu.com \
    --ProjectId 0 \
    --ServiceType web \
    --Domain test04.lukachen.work \
    --Area mainland
```

Output: 
```
{
    "Response": {
        "RequestId": "281e0d75-d2df-4039-bad2-79c0f753baf9"
    }
}
```

