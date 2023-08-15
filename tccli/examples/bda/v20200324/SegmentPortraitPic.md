**Example 1: 调用失败示例**



Input: 

```
tccli bda SegmentPortraitPic --cli-unfold-argument  \
    --Url IamNotAUrl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.UrlIllegal",
            "Message": "URL格式不合法。"
        },
        "RequestId": "46ed6f32-549f-4377-8116-2d55e4574528"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda SegmentPortraitPic --cli-unfold-argument  \
    --Url test.jpg
```

Output: 
```
{
    "Response": {
        "ResultImage": "iVBORw0KGgoAAAANSUhEUgAAAiYAAAFuCAYAAAC1LdPaAAAgAElEQVR4AbTB0ZJlyXUYy4g8DT1hICNl5P9/50WdFdJqWIJ7ioWahnDl7r/99me+MzM8VTwNh39FxWcqS+Wcw3cqLpUnlUtFZamorMPvqaiorJlBReWcg4rKUuk9/DMqKirWaVCpWBUVFRVXRcWTysi3KpbKUlkq68TfqaioLJWZQWWpqCyVz1SeVN7vN/+IgA4UIaui4vp4x1UxHlbFer//ylWxKr5SsSpWRULFk8pSUXlS+YrKUlkqS0VFZVUsFZWOLBUVFRWVpaKiUlGxVFR+eKioqFBRUVGZGb6jsSqeKtbM8KTyJN8757BUVkVFxTrn8KTyVKHypH...",
        "ResultMask": "...XWPBHiy5s9MsfGWqRxIlxe+DdQbyLK9a6lDSLpaFbtC21I3GK/okoooooooooooooooooooooooor+Qb/g73/bN1j4HfsbeCP2evCt7qum6x8e9cuDrN5YnT3spfDWi8T6bfrOHvImnnbfHJbKmQMM/av8AMAJJJJOSeST1J9TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRXV+BvHPi/wCGni3QPHfgPxDqfhXxf4X1K11jQPEGjXUlnqWl6lZyrNbXdrcREPHLFIoYHocYIIJFf7FX/BAn9qf41fthf8E2fgz8Y/j74oXxl8RdRivtL1LxE1lBZXOow6XcPaW096tviOa8aKNTPcbVaaTLsMk1+0dFFFFFFFFFFFFFFFFFFFFFFFf5jX/B5jqOoSft8fCfTZL68fToPg3p88Fg9zO1lDPJqFwJJorUuYI5ZAAHkSMOwADE4r+Oyiiiiv/Z",
        "HasForeground": true,
        "ResultMaskUrl": "",
        "ResultImageUrl": "",
        "RequestId": "9cf173a5-4ae5-46fb-9898-6c876263780d"
    }
}
```

