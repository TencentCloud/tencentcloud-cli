**Example 1: 按文本在知识库中进行搜索**



Input: 

```
tccli vod SearchMediaBySemantics --cli-unfold-argument  \
    --SubAppId 1000000000 \
    --Text 关于冬天的视频 \
    --KnowledgeBaseId kb-**********
```

Output: 
```
{
    "Response": {
        "SearchResults": [
            {
                "EndTimeOffset": 46.758,
                "FileId": "966263618988054694",
                "Score": 0.17525,
                "StartTimeOffset": 1.9729999999999999
            }
        ],
        "RequestId": "c82ee200-498a-4def-9985-809e43b7e16b"
    }
}
```

**Example 2: 按图片FileId在知识库中进行搜索**

注意：KnowledgeBaseId对应的知识库必须为图片知识库

Input: 

```
tccli vod SearchMediaBySemantics --cli-unfold-argument  \
    --SubAppId 200000 \
    --FileId 9****************1 \
    --KnowledgeBaseId kb-**********
```

Output: 
```
{
    "Response": {
        "SearchResults": [
            {
                "EndTimeOffset": 0,
                "FileId": "9****************1",
                "Score": 1,
                "StartTimeOffset": 0,
                "Title": ""
            }
        ],
        "RequestId": "71e66da3-abd4-4024-91e1-a596df4f719b"
    }
}
```

**Example 3: 按图片Url在知识库中进行搜索**

注意：KnowledgeBaseId对应的知识库必须为图片知识库

Input: 

```
tccli vod SearchMediaBySemantics --cli-unfold-argument  \
    --SubAppId 200000 \
    --Url https://******************.cos.ap-shanghai.myqcloud.com/***********.png \
    --KnowledgeBaseId kb-**********
```

Output: 
```
{
    "Response": {
        "SearchResults": [
            {
                "EndTimeOffset": 0,
                "FileId": "9****************1",
                "Score": 1,
                "StartTimeOffset": 0,
                "Title": ""
            }
        ],
        "RequestId": "dccae516-7f4e-4972-90dc-36a5c22361d3"
    }
}
```

