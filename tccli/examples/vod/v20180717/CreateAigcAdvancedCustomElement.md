**Example 1: 创建多图主体**



Input: 

```
tccli vod CreateAigcAdvancedCustomElement --cli-unfold-argument  \
    --SubAppId 221073 \
    --ElementName testname \
    --ElementDescription testdescription \
    --ReferenceType image_refer \
    --ElementVoiceId 123333 \
    --ElementImageList {"frontal_image":"image_url_0","refer_images":[{"image_url":"image_url_1"},{"image_url":"image_url_2"},{"image_url":"image_url_3"}]} \
    --TagList [{"tag_id": "o_101"}, {"tag_id": "o_102"}]
```

Output: 
```
{
    "Response": {
        "TaskId": "221073-CreateAigcAdvancedCustomElement-927af0f45e354127835f6ec67c48f2a9t",
        "RequestId": "2ff6980c-db91-488b-bb5b-04e8eb5661d2"
    }
}
```

