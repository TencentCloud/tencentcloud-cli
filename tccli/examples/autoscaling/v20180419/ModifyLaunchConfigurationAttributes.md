**Example 1: 清空UserData**

指定启动配置asc-291kq6ku，将UserData修改为空字符串

Input: 

```
tccli as ModifyLaunchConfigurationAttributes --cli-unfold-argument  \
    --LaunchConfigurationId asc-291kq6ku \
    --UserData 
```

Output: 
```
{
    "Response": {
        "RequestId": "2c027f22-3a3b-489a-a77a-89c53fc15212"
    }
}
```

**Example 2: 指定启动配置，修改镜像、实例类型、名称**

指定启动配置asc-291kq6ku，修改镜像为img-8toqc6s3，修改实例类型为S2.SMALL1，修改启动配置名称为updated_config

Input: 

```
tccli as ModifyLaunchConfigurationAttributes --cli-unfold-argument  \
    --ImageId img-8toqc6s3 \
    --InstanceTypes S2.SMALL1 \
    --LaunchConfigurationName updated_config \
    --LaunchConfigurationId asc-291kq6ku
```

Output: 
```
{
    "Response": {
        "RequestId": "07022dcb-5bba-48f0-a2b0-800ad006d031"
    }
}
```

