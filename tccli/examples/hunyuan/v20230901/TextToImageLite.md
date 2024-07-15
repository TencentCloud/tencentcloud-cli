**Example 1: 成功调用**

成功调用，并返回生图url

Input: 

```
tccli hunyuan TextToImageLite --cli-unfold-argument  \
    --Prompt 冰川，企鹅 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "53549a10-0633-4ebe-bf39-466dc51aa2bb",
        "ResultImage": "https://rspimg.jpg"
    }
}
```

