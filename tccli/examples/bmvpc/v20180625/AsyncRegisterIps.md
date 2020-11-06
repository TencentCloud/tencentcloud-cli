**Example 1: 批量注册虚拟IP(异步接口)**

创建了虚拟子网或者DOCKER子网，要使用子网的IP，首先需要注册IP

Input: 

```
tccli bmvpc AsyncRegisterIps --cli-unfold-argument  \
    --VpcId vpc-xxxx \
    --SubnetId subnet-6tgv9t88 \
    --Ips 10.10.245.162
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "c3c16932-2531-4535-8303-ffb2081315ae"
    }
}
```

