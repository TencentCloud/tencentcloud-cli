**Example 1: Getting keyword sample list - with no filters**

This example shows you how to traverse the list of keywords with no filters.

Input: 

```
tccli mps DescribeWordSamples --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "WordSet": [
            {
                "Keyword": "John Smith",
                "TagSet": [
                    "Celebrity",
                    "Artist"
                ],
                "Usages": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z"
            },
            {
                "Keyword": "Jane Smith",
                "TagSet": [
                    "President"
                ],
                "Usages": [
                    "Review.Ocr",
                    "Review.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 2: Getting keyword sample list - with filters**

This example shows you how to query keyword samples with filters such as the specified use case.

Input: 

```
tccli mps DescribeWordSamples --cli-unfold-argument  \
    --Usages Recognition Review.Ocr \
    --Keywords 'John Smith' \
    --Tags Celebrity \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WordSet": [
            {
                "Keyword": "John Smith",
                "TagSet": [
                    "Celebrity",
                    "Artist"
                ],
                "Usages": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

