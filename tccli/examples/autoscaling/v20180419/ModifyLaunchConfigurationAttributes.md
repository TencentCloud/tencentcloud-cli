**Example 1: 指定启动配置，修改镜像、实例类型、名称**



Input: 

```
tccli as ModifyLaunchConfigurationAttributes --cli-unfold-argument  \
    --LaunchConfigurationId asc-291kq6ku\
    --ImageId img-8toqc6s3\
    --InstanceTypes S2.SMALL1\
    --LaunchConfigurationName updated_config
```

Output: 
```
{
    "Response": {
        "RequestId": "07022dcb-5bba-48f0-a2b0-800ad006d031"
    }
}
```

**Example 2: 清空UserData**



Input: 

```
tccli as ModifyLaunchConfigurationAttributes --cli-unfold-argument  \
    --LaunchConfigurationId asc-291kq6ku\
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

