**Example 1: 创建资源栈**



Input: 

```
tccli tic CreateStack --cli-unfold-argument  \
    --StackName web-service \
    --TemplateUrl https://xxx.cos.ap-guangzhou.myqcloud.com/terraform.zip \
    --Description an awesome mysql/go/nginx web server stack \
    --StackRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "StackId": "stk-wt1ln3to",
        "VersionId": "ver-kg8hn58h",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

