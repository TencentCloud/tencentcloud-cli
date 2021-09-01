**Example 1: 清空启动配置中的数据盘项**



Input: 

```
tccli as ClearLaunchConfigurationAttributes --cli-unfold-argument  \
    --LaunchConfigurationId asc-kr4beurf \
    --ClearDataDisks True
```

Output: 
```
{
    "Response": {
        "RequestId": "382c6cad-15ae-496a-a965-66b95674f5a7"
    }
}
```

