**Example 1: Reinstalling an instance**

This example shows you how to reinstall an instance with the image, login password, and enhanced services specified, and expand the system disk of the instance.

Input: 

```
tccli cvm ResetInstance --cli-unfold-argument  \
    --InstanceId ins-r8hr2upy \
    --ImageId img-pmqg1cw7 \
    --SystemDisk.DiskSize 60 \
    --LoginSettings.Password Qcloud@TestApi123++ \
    --EnhancedService.SecurityService.Enabled TRUE \
    --EnhancedService.MonitorService.Enabled TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "a0a66377-b79f-4a21-846c-d997d6022968"
    }
}
```

