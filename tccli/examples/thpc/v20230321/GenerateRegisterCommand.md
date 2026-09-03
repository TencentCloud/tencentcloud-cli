**Example 1: 生成IDC集群节点注册命令（直连）**

为可直连的IDC集群生成节点注册命令。

Input: 

```
tccli thpc GenerateRegisterCommand --cli-unfold-argument  \
    --ClusterId hpc-12345678
```

Output: 
```
{
    "Response": {
        "RegisterCommand": "curl -sSL http://xxx/register.sh | bash -s -- --code eyJ...",
        "RegisterCode": "eyJhbGciOiJIUzI1NiJ9...",
        "ExpireAt": 1755676800,
        "Proxy": false,
        "ClusterId": "hpc-12345678",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

**Example 2: 生成IDC集群节点注册命令（走专线代理）**

为IDC集群生成经专线代理接入的节点注册命令。

Input: 

```
tccli thpc GenerateRegisterCommand --cli-unfold-argument  \
    --ClusterId hpc-12345678 \
    --Proxy True \
    --VpcId vpc-aaaa1234 \
    --SubnetId subnet-bbbb5678
```

Output: 
```
{
    "Response": {
        "RegisterCommand": "curl -sSL http://xxx/register.sh | bash -s -- --code eyJ...",
        "RegisterCode": "eyJhbGciOiJIUzI1NiJ9...",
        "ExpireAt": 1755676800,
        "Proxy": true,
        "EndPointVip": "10.0.0.1",
        "EndPointStatus": "ACTIVE",
        "ClusterId": "hpc-12345678",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

