**Example 1: 创建函数**



Input: 

```
tccli tcb CreateFunction --cli-unfold-argument  \
    --FunctionName my-func \
    --EnvId env-zyxjgkd \
    --Handler index.main \
    --MemorySize 0 \
    --Timeout 0 \
    --UseGpu FALSE \
    --InstallDependency TRUE \
    --Stamp Tcb \
    --Role TCB_QcsRole \
    --Description my function \
    --Runtime nodejs16 \
    --ClsTopicId topic-xx \
    --ClsLogsetId logset-yy \
    --Code.ZipFile zip-code-here \
    --PrivateConfig.Language nodejs
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 创建函数0824**



Input: 

```
tccli tcb CreateFunction --cli-unfold-argument  \
    --FunctionName jackvylitest2 \
    --EnvId cbftest-goreliu-d5f0c7kud1ee02a6 \
    --Handler index.main \
    --MemorySize 256 \
    --Timeout 3 \
    --UseGpu FALSE \
    --InstallDependency TRUE \
    --Runtime Nodejs24.14 \
    --Code.ZipFile UEsDBBQAAAAIAKyFGF0rzojg8AAAAEIBAAAIABwAaW5kZXguanNVVAkAA6MEjGqkBIxqdXgLAAEE9QEAAAQUAAAAXY89TsNAEIV7n+JV2VgydkTpKBREQoICCg6ANt6xs7DeMbvrKJblkppDII6We2A7pIk0xfzove9NlmFruFX30hMeWlsEzRanr9/T909Ex4Zd8GkttcUG0ne2wJIOZEOCgm2gY4ixuUMfYZo9G0oNV0tR7EooqhnaHviDlEjw9PrynPrgtK102Z1d4ng9Kh2F1tnZBPBBhtZvWVGO29UqmZd7koqcz9FDzFwbbkLXkMghZNMYXcgpd/bu2QoMZ9GOVZdfY3vU5L2sRnexJ2MYpeMaY94xoqPPlnx4VPnlOywWlzb9v75phSGeEMM6GusPUEsDBBQAAAAIAKyFGF2amvlBfwAAALoAAAAMABwAcGFja2FnZS5qc29uVVQJAAOjBIxqowSManV4CwABBPUBAAAEFAAAAD2OSwoCMQxA9z1FyFrKuHWpILhw5wVKG6EyTaXJiDDM3e1ncJn3XkJWA4DsEuEJ8Lmw15hZSRQPzXyoSAVNHu1kp0EDiS/xrbu5zHkJZycE1/0ABEp5tMnFHkUO9LUvGXTsSxVrHRtQV7R1nAPBP65y6wtz9MTSv7zfHmg28wNQSwECHgMUAAAACACshRhdK86I4PAAAABCAQAACAAYAAAAAAABAAAApIEAAAAAaW5kZXguanNVVAUAA6MEjGp1eAsAAQT1AQAABBQAAABQSwECHgMUAAAACACshRhdmpr5QX8AAAC6AAAADAAYAAAAAAABAAAApIEyAQAAcGFja2FnZS5qc29uVVQFAAOjBIxqdXgLAAEE9QEAAAQUAAAAUEsFBgAAAAACAAIAoAAAAPcBAAAAAA==
 \
    --VpcConfig.VpcId vpc-3m4f4bhq \
    --VpcConfig.SubnetId subnet-2tvkenrt \
    --Layers.0.LayerName demo \
    --Layers.0.LayerVersion 1
```

Output: 
```
{
    "Response": {
        "SCFErrorCode": "",
        "SCFErrorMsg": "",
        "RequestId": "cc908925-479f-4ed5-ab49-bc2c6466bd92"
    }
}
```

