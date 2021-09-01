**Example 1: 创建自定义镜像**



Input: 

```
tccli bm CreateCustomImage --cli-unfold-argument  \
    --InstanceId testid \
    --ImageName aa678 \
    --ImageDescription 876aa
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c",
        "TaskId": 123,
        "ImageId": "bm-img-1a2b3c4d"
    }
}
```

