**Example 1: Creating keyword sample - All**

If `Usages` is `All`, then this keyword can be used for OCR-based and ASR-based content recognition and audit.

Input: 

```
tccli vod CreateWordSamples --cli-unfold-argument  \
    --Usages All\
    --Words.0.Keyword Influencer\
    --Words.0.Tags Entertainment
```

Output: 
```
{
    "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
}
```

**Example 2: Creating keyword sample - Recognition**

If `Usages` is `["Recognition.Ocr","Review.Ocr"]`, then this keyword can be used for OCR-based content recognition and audit.

Input: 

```
tccli vod CreateWordSamples --cli-unfold-argument  \
    --Usages Recognition.Ocr Review.Ocr\
    --Words.0.Keyword Influencer\
    --Words.0.Tags Entertainment
```

Output: 
```
{
    "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
}
```

**Example 3: Creating keyword sample - Review**

If `Usages` is `Review`, then this keyword can be used for OCR-based and ASR-based content audit.

Input: 

```
tccli vod CreateWordSamples --cli-unfold-argument  \
    --Usages Review\
    --Words.0.Keyword 'John Smith'\
    --Words.0.Tags 'Politically sensitive'
```

Output: 
```
{
    "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
}
```

