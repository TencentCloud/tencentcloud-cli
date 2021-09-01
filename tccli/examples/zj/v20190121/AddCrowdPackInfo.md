**Example 1: AddCrowdPackInfo**



Input: 

```
tccli zj AddCrowdPackInfo --cli-unfold-argument  \
    --Name aaa \
    --FileName aaa.txt \
    --Desc 0 \
    --PhoneNum 0 \
    --CosUrl "http:/xxx.cos.ap-shanghai.myqcloud.com/xxx/5ce38bcc-969f-4963-995d-4126065f3700.txt" \
    --License xsdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": 1
        },
        "RequestId": "111111"
    }
}
```

