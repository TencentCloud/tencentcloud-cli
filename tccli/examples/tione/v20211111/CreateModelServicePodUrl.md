**Example 1: 创建在线服务登陆pod链接**

登陆在线服务pod进行调试

Input: 

```
tccli tione CreateModelServicePodUrl --cli-unfold-argument  \
    --ServiceId ms-thisisatest \
    --PodName ms-thisisatest-podname
```

Output: 
```
{
    "Response": {
        "Url": "http://dfsdfxx",
        "RequestId": "a-fake-id"
    }
}
```

