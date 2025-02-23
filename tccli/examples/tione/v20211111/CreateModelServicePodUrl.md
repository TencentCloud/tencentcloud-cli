**Example 1: 创建在线服务登陆pod链接**

登陆在线服务pod进行调试

Input: 

```
tccli tione CreateModelServicePodUrl --cli-unfold-argument  \
    --ServiceId abc \
    --PodName abc
```

Output: 
```
{
    "Response": {
        "Url": "abc",
        "RequestId": "abc"
    }
}
```

