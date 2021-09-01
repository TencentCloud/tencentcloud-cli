**Example 1: 修改镜像名称**

修改镜像img-6pb6lrmy的名称为sample

Input: 

```
tccli cvm ModifyImageAttribute --cli-unfold-argument  \
    --ImageId img-6pb6lrmy \
    --ImageName sample
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

