**Example 1: 批量修改后端服务的权重**

针对负载均衡实例(lb-dx98lwo0)， 将其监听器 lbl-4b5hnc9a 下的转发规则 loc-o8cnyw6c 所绑定的后端服务 ins-19404pl5（端口为110）权重修改为 50，以及将监听器 lbl-20jjtaaw 下的转发规则 loc-8c5pdrb8 所绑定的后端服务 ins-19411tzv（端口为80）权重修改为 30

Input: 

```
tccli clb BatchModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-dx98lwo0 \
    --ModifyList.0.ListenerId lbl-4b5hnc9a \
    --ModifyList.0.LocationId loc-o8cnyw6c \
    --ModifyList.0.Targets.0.InstanceId ins-19404pl5 \
    --ModifyList.0.Targets.0.Port 110 \
    --ModifyList.0.Targets.0.Weight 50 \
    --ModifyList.1.ListenerId lbl-20jjtaaw \
    --ModifyList.1.LocationId loc-8c5pdrb8 \
    --ModifyList.1.Targets.0.InstanceId ins-19411tzv \
    --ModifyList.1.Targets.0.Port 80 \
    --ModifyList.1.Targets.0.Weight 30
```

Output: 
```
{
    "Response": {
        "RequestId": "83329908-a282-4f9f-8ab-031a3025b377"
    }
}
```

**Example 2: 批量修改四层和七层监听器绑定的服务器权重**

同时对一个负载均衡下的四层和七层监听器修改所绑定的服务器权重

Input: 

```
tccli clb BatchModifyTargetWeight --cli-unfold-argument  \
    --LoadBalancerId lb-1kkno9qf \
    --ModifyList.0.ListenerId lbl-mhtffs09 \
    --ModifyList.0.Targets.0.InstanceId ins-kjp6cb2f \
    --ModifyList.0.Targets.0.Port 79 \
    --ModifyList.0.Targets.0.Weight 50 \
    --ModifyList.1.ListenerId lbl-661zpn3b \
    --ModifyList.1.LocationId loc-78p1r0vb \
    --ModifyList.1.Targets.0.EniIp 10.202.0.96 \
    --ModifyList.1.Targets.0.Port 123 \
    --ModifyList.1.Targets.0.Weight 30
```

Output: 
```
{
    "Response": {
        "RequestId": "38bab2ce-616d-412c-a4b0-36110d5b17a3"
    }
}
```

