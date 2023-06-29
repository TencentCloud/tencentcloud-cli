**Example 1: 查询平行容器安装命令**

查询平行容器安装命令

Input: 

```
tccli tcss DescribeAgentDaemonSetCmd --cli-unfold-argument  \
    --IsCloud true \
    --NetType "basic"
```

Output: 
```
{
    "Response": {
        "Command": "abc",
        "RequestId": "abc"
    }
}
```

