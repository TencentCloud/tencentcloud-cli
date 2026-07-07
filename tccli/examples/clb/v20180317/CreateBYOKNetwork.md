**Example 1: 初始化BYOK VPC网络**

初始化 VPC 网络，返回 ServiceProviderId 供后续 CreateModel 使用

Input: 

```
tccli clb CreateBYOKNetwork --cli-unfold-argument  \
    --VpcId vpc-abcd1234 \
    --SubnetId subnet-efgh5678 \
    --ServiceProviderName my-vpc-model
```

Output: 
```
{
    "Response": {
        "RequestId": "b521a934-0358-497a-8e3a-f1242424747c"
    }
}
```

**Example 2: 初始化BYOK VPC网络（带标签）**

初始化 VPC 网络并绑定标签

Input: 

```
tccli clb CreateBYOKNetwork --cli-unfold-argument  \
    --VpcId vpc-abcd1234 \
    --SubnetId subnet-efgh5678 \
    --ServiceProviderName my-vpc-model
```

Output: 
```
{
    "Response": {
        "RequestId": "c632b045-1469-508b-9f4b-g2353535858d"
    }
}
```

