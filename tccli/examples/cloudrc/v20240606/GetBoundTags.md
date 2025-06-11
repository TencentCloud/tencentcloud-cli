**Example 1: 获取已绑定资源的标签集合**



Input: 

```
tccli cloudrc GetBoundTags --cli-unfold-argument  \
    --ViewId vw-6wyborpx
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Key": "project",
                "Value": "默认项目"
            },
            {
                "Key": "应用",
                "Value": "应用1"
            },
            {
                "Key": "应用",
                "Value": "应用2"
            },
            {
                "Key": "应用",
                "Value": "应用3"
            }
        ],
        "RequestId": "435a7333-c9c9-48fb-80e0-02099fbf1d48"
    }
}
```

