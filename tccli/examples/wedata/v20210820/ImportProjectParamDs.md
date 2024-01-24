**Example 1: 导入项目参数**

导入项目参数

Input: 

```
tccli wedata ImportProjectParamDs --cli-unfold-argument  \
    --ProjectId abc \
    --FileName xxxx.json
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

