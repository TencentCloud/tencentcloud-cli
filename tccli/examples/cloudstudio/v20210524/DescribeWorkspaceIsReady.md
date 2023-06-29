**Example 1: 获取工作空间是否已经启动就绪**

获取工作空间是否已经启动就绪

Input: 

```
tccli cloudstudio DescribeWorkspaceIsReady --cli-unfold-argument  \
    --SpaceKey abcx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

