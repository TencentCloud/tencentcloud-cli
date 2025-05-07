**Example 1: hai实例制作自定义应用**

对创建成功的HAI实例进行自定义应用制作。

Input: 

```
tccli hai CreateApplication --cli-unfold-argument  \
    --InstanceId hai-3nagq120 \
    --ApplicationName My Application \
    --ApplicationDescription This is my first pytorch HAI application.
```

Output: 
```
{
    "Response": {
        "ApplicationId": "app-az05wwqa",
        "RequestId": "83697e89-90d2-4fff-bbb1-1bc3d53c4dfadfdad"
    }
}
```

