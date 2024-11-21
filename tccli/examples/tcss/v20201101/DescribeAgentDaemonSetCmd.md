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
        "Command": "install command'",
        "FileContent": "fakecontent",
        "RequestId": "0adc9022-1364-4b4b-b3e7-2e37930af279",
        "URL": "https://1.2.3.4/a"
    }
}
```

