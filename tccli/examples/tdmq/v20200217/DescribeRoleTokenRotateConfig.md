**Example 1: 查询是否开启轮转**



Input: 

```
tccli tdmq DescribeRoleTokenRotateConfig --cli-unfold-argument  \
    --SecretName asddasammasdads \
    --UserResourceId pulsar-g4de9kbzxxoz \
    --ResourceAccount autoRole1 \
    --InstanceType Pulsar
```

Output: 
```
{
    "Response": {
        "EnabledRotate": true,
        "RequestId": "5ce3109e-595c-4849-933f-f1da9656e15e"
    }
}
```

