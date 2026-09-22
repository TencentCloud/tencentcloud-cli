**Example 1: 创建资源图谱**



Input: 

```
tccli cls CreateResourceGraph --cli-unfold-argument  \
    --Name 生产环境-test-2 \
    --Description 生产环境资源空间 \
    --Tags.0.Key name \
    --Tags.0.Value 业务A
```

Output: 
```
{
    "Response": {
        "ResourceGraphId": "8c0433ae-a1bb-479a-a0fb-592560e3d22a",
        "RequestId": "8cd9d427-f94c-4d6b-81d9-121952d4c0a8"
    }
}
```

