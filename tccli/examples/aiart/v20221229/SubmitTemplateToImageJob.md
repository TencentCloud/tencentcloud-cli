**Example 1: 调用成功示例**



Input: 

```
tccli aiart SubmitTemplateToImageJob --cli-unfold-argument  \
    --Image.Url https://test.com/1.png \
    --Style gallerying \
    --LogoAdd 1
```

Output: 
```
{
    "Response": {
        "JobId": "1394637692053602304",
        "RequestId": "b1759140-6951-4d6a-9f12-add42ca16b25"
    }
}
```

