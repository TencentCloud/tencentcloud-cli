**Example 1: 创建个人版环境**

创建个人版环境(PackageId=baas_personal)，并指定包含 文档型数据库(flexdb)、云存储(storage)、云函数(function) 三种资源。
购买周期为1个月(Period=1)。
自动使用代金券支付(AutoVoucher=true)。
环境别名为 cloudbase(Alias=cloudbase)。
创建成功，则自动拿到一个以 Alias(当前值为cloudbase) 为前缀的 EnvId：cloudbase-8grqda2hfc2f62bb

Input: 

```
tccli tcb CreateEnv --cli-unfold-argument  \
    --Alias cloudbase \
    --PackageId baas_personal \
    --Resources flexdb storage function \
    --Period 1 \
    --AutoVoucher True
```

Output: 
```
{
    "Response": {
        "EnvId": "cloudbase-8grqda2hfc2f62bb",
        "RequestId": "53d30c8d-53ba-46c0-89a5-c791ad79a2b8"
    }
}
```

