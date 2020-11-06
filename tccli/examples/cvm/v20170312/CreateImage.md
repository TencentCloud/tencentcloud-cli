**Example 1: 创建一个镜像**

使用实例ins-6pb6lrmy 创建一个镜像。当实例处于运行中时，执行软关机，软关机失败后，结束任务(默认语义)。

Input: 

```
tccli cvm CreateImage --cli-unfold-argument  \
    --InstanceId ins-6pb6lrmy \
    --ImageName "name"
```

Output: 
```
{
    "Response": {
        "ImageId": "img-0yc6rie8",
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

