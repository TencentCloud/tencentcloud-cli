**Example 1: 多图像识别批改-识别**

ServerType = 0，使用识别功能，只返回识别文本。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": " Dear Peter,\n I am glad to hear from you. Let me tell you something about Nanjing.\nFirst, the environment in Nanjing is beautiful and there are many trees on both sides an of the road\nNext ,it's very easy to travel around the city and there are many ways. People all have a confortable life,here are lots of tall buildings for or them to live.\nWhat's more, Nanjing has many interesting places and lots of visiters come here every year.\nAll in all, Nanjing is a good place to visit Yours sincerely, and I hope you can visit it some day Su Hua\n  Dear Peter,\n I am glad to hear from you. Let me tell you something about Nanjing.\nNanjing is a clean and beautiful city. There a are many trees and mountains. Also, people here live a happy life. They live in comfortable flaks and communicate with their friends easily. And the transport changes. When people want to go out and\ntaxi they can take a or an underground Furthermore, Naying is a good place to travel. There are many places of interest. You can a visit Xuanoun Park. You can see many views in it. All in all, I think Nanjing is a peaceful and Yours sincerely, perfect city. I hope it can be better\nand better. Su Hua\n",
            "CorrectData": null,
            "TaskId": "",
            "SessionId": ""
        },
        "RequestId": "4cd778bd-4e62-44a3-bd6a-27686c2af81d"
    }
}
```

**Example 2: 多图像识别批改-批改**

ServerType = 1，使用批改功能，只返回批改结果。
注意：图像批改耗时较长，超过4s后返回异步任务结果。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6560fa28-683e-454f-b8a2-88bee017836a"
    }
}
```

**Example 3: 多图像识别批改-异步批改**

ServerType = 1，使用批改功能，只返回批改结果。
IsAsync= 1，使用异步处理。

Input: 

```
tccli ecc CorrectMultiImage --cli-unfold-argument  \
    --InputType 0 \
    --Image https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/0999.jpg https://ecc-access-file-test-1253364609.cos.ap-guangzhou.myqcloud.com/1000.jpg \
    --ServerType 1 \
    --IsAsync 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": "",
            "CorrectData": null,
            "TaskId": "10001265",
            "SessionId": ""
        },
        "RequestId": "1d417477-05cb-409e-b4bf-b4a4842ef513"
    }
}
```

