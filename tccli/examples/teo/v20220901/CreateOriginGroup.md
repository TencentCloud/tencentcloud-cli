**Example 1: 创建按权重回源的自有源站组**

此源站组可以给四层代理规则和负载均衡使用，其中四层代理规则源站组OriginType只能为self，且源站必须填写端口。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforl4 \
    --ConfigurationType weight \
    --OriginType self \
    --OriginRecords.0.Record 1.2.3.4 \
    --OriginRecords.0.Weight 50 \
    --OriginRecords.0.Port 80 \
    --OriginRecords.1.Record 1.2.3.5 \
    --OriginRecords.1.Weight 50 \
    --OriginRecords.1.Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 2: 创建按权重回源的自有源站组（默认端口）**

此源站组适合负载均衡使用。参数中未填写Weight值，将按照轮询的方式，即平均分配权重的方式回源。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType weight \
    --OriginType self \
    --OriginRecords.0.Record 1.2.3.4 \
    --OriginRecords.1.Record 1.2.3.5
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 3: 创建按协议回源的自有源站组（指定协议和端口）**

此源站组适合负载均衡使用。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType proto \
    --OriginType self \
    --OriginRecords.0.Record 1.2.3.4 \
    --OriginRecords.0.Proto http \
    --OriginRecords.0.Port 80 \
    --OriginRecords.1.Record 1.2.3.5 \
    --OriginRecords.1.Proto https \
    --OriginRecords.1.Port 443
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 4: 创建公有鉴权的AWS对象存储源站组**

此源站组适合负载均衡使用。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType  \
    --OriginType third_party \
    --OriginRecords.0.Record your-name.s3.us-east-1.amazonaws.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 5: 创建私有鉴权的AWS对象存储源站组**

此源站组适合负载均衡使用。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType  \
    --OriginType third_party \
    --OriginRecords.0.Record your-name.s3.us-east-1.amazonaws.com \
    --OriginRecords.0.Private True \
    --OriginRecords.0.PrivateParameters.0.Name AccessKeyId \
    --OriginRecords.0.PrivateParameters.0.Value your aws access key id \
    --OriginRecords.0.PrivateParameters.1.Name SecretAccessKey \
    --OriginRecords.0.PrivateParameters.1.Value your aws secret access key
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 6: 创建公有鉴权的腾讯云COS源站组**

此源站组适合负载均衡使用。
注意：依赖COS产品部分操作对Edgeone产品的授权，可在控制台上相应模块进行授权。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType  \
    --OriginType cos \
    --OriginRecords.0.Record your-name.cos.ap-nanjing.myqcloud.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

**Example 7: 创建私有鉴权的腾讯云COS源站组**

此源站组适合负载均衡使用。
注意：依赖COS产品部分操作对Edgeone产品的授权，可在控制台上相应模块进行授权。

Input: 

```
tccli teo CreateOriginGroup --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --OriginGroupName origingroupforloadbalancing \
    --ConfigurationType  \
    --OriginType cos \
    --OriginRecords.0.Record your-name.cos.ap-nanjing.myqcloud.com \
    --OriginRecords.0.Private True
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "OriginGroupId": "origin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a"
    }
}
```

