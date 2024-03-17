**Example 1: 修改配置文件**

修改配置文件

Input: 

```
tccli tse ModifyConfigFiles --cli-unfold-argument  \
    --InstanceId abc \
    --ConfigFile.Id 1 \
    --ConfigFile.Name abc \
    --ConfigFile.Namespace abc \
    --ConfigFile.Group abc \
    --ConfigFile.Content abc \
    --ConfigFile.Format abc \
    --ConfigFile.Comment abc \
    --ConfigFile.Status abc \
    --ConfigFile.Tags.0.Key abc \
    --ConfigFile.Tags.0.Value abc \
    --ConfigFile.CreateTime abc \
    --ConfigFile.CreateBy abc \
    --ConfigFile.ModifyTime abc \
    --ConfigFile.ModifyBy abc \
    --ConfigFile.ReleaseTime abc \
    --ConfigFile.ReleaseBy abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

