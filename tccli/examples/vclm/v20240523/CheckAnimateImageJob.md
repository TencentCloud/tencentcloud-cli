**Example 1: 检测输入图成功案例**

检测输入图成功案例

Input: 

```
tccli vclm CheckAnimateImageJob --cli-unfold-argument  \
    --TemplateId ke3 \
    --ImageUrl https://tencent.cos.ap-guangzhou.myqcloud.com/image-animate/user_input/image.png \
    --EnableBodyJoins True
```

Output: 
```
{
    "Response": {
        "CheckPass": true,
        "RequestId": "96c02249-a683-4c0b-ac1c-50a2dee71695"
    }
}
```

