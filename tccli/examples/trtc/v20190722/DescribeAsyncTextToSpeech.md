**Example 1: 查询例子**



Input: 

```
tccli trtc DescribeAsyncTextToSpeech --cli-unfold-argument  \
    --TaskId 86edb448-dc2f-4853-be31-8f05c7d3f6fe
```

Output: 
```
{
    "Response": {
        "AudioDownloadUrl": "https://async-tts-1258344699.cos.ap-shanghai.myqcloud.com/86edb448-dc2f-4853-be31-8f05c7d3f6fe/result.m****-sign-algorithm=sha1&************************************KhndC&q-**gn-time=1775910013%3B1775942413&q-key-time=1775910013%3B1775942413&q-header-list=host&q-url-param-list=&q-signature=6618730ea4953adf7912d4d5188eeff0ee56cfa9",
        "Status": "Success",
        "SubtitleDownloadUrl": "https://async-tts-1258344699.cos.ap-shanghai.myqcloud.com/86edb448-dc2f-4853-be31-8f05c7d3f6fe/subtitle.json?******-algorithm=sha1&******************U***hphJfkY5MM6Zlg***dC&q-sign-time=1775910013%3B1775942413&q-key-time=1775910013%3B1775942413&q-header-list=host&q-url-param-list=&q-signature=32d59684e4cb9884c38b8d32f1b1dfbfac1ae42f",
        "RequestId": "ec74e0f9-1921-4781-87d3-b724d9b9a1d1"
    }
}
```

