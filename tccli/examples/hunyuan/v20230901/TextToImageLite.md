**Example 1: 成功调用**

成功调用，并返回生图url

Input: 

```
tccli hunyuan TextToImageLite --cli-unfold-argument  \
    --Prompt 雨中, 竹林,  小路 \
    --RspImgType url
```

Output: 
```
{
    "Response": {
        "RequestId": "53549a10-0633-4ebe-bf39-466dc51aa2bb",
        "ResultImage": "https://hyimg-xxx.cos.ap-guangzhou.myqcloud.com/xxx.jpg?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1731586602;1731590202&q-key-time=1731586602;1731590202&q-header-list=host&q-url-param-list=&q-signature=ebb3f1d327cf4224c798ef328e1babbb41d09326"
    }
}
```

