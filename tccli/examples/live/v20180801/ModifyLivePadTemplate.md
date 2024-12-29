**Example 1: 请求示例**



Input: 

```
tccli live ModifyLivePadTemplate --cli-unfold-argument  \
    --Description padtemplate \
    --TemplateName mytemplate \
    --Url http://mypad.file.com/pad/file.mp4 \
    --WaitDuration 1 \
    --TemplateId 1 \
    --MaxDuration 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

