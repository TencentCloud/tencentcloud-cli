**Example 1: 调用成功示例**

调用成功示例

Input: 

```
tccli vclm SubmitImageAnimateJob --cli-unfold-argument  \
    --ImageUrl https://xxx/image-animate/user_input/1.png \
    --TemplateId ke3 \
    --EnableAudio True
```

Output: 
```
{
    "Response": {
        "JobId": "1194931538865782784",
        "RequestId": "4e6722ba-367b-454e-add0-681a5c50fe20"
    }
}
```

