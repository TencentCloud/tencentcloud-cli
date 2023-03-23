**Example 1: 清空启动配置中的数据盘项**

指定启动配置asc-kr4beurf，入参ClearDataDisks设置为true，接口调用后启动配置中的数据盘信息被清空，后续基于asc-kr4beurf创建的云主机将不再分配任何数据盘

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

