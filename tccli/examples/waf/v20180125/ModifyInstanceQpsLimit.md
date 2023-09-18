**Example 1: 设置套餐实例的弹性qps上限示例**



Input: 

```
tccli waf ModifyInstanceQpsLimit --cli-unfold-argument  \
    --InstanceId waf_2kugtqmk020i74z5 \
    --QpsLimit 100000
```

Output: 
```
{
    "Response": {
        "RequestId": "93c70d0b-624e-46c7-95b5-2269818e65be"
    }
}
```

