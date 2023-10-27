**Example 1: 重装实例**

本示例用于指定镜像、登录密码和增强服务来重装实例，同时扩容实例系统盘。

Input: 

```
tccli cvm ResetInstance --cli-unfold-argument  \
    --InstanceId ins-r8hr2upy \
    --SystemDisk.DiskSize 60 \
    --EnhancedService.SecurityService.Enabled True \
    --EnhancedService.MonitorService.Enabled True \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --ImageId img-pmqg1cw7
```

Output: 
```
{
    "Response": {
        "RequestId": "a0a66377-b79f-4a21-846c-d997d6022968"
    }
}
```

