**Example 1: 创建镜像**



Input: 

```
tccli ecm CreateImage --cli-unfold-argument  \
    --InstanceId ein-93sjjr8k \
    --ImageName test_name \
    --ImageDescription test_description \
    --ForcePoweroff TRUE
```

Output: 
```
{
    "Response": {
        "TaskId": "1528611",
        "RequestId": "a3c3e99e-c4d7-11ea-ba2d-52540002f896"
    }
}
```

