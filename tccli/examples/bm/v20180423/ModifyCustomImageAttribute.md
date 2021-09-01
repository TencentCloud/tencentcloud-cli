**Example 1: 修改自定义镜像别名或备注**



Input: 

```
tccli bm ModifyCustomImageAttribute --cli-unfold-argument  \
    --ImageId testid \
    --ImageName aa678 \
    --ImageDescription 876aa
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a13989-5776-4a8b-83d6-43714117ac3c"
    }
}
```

