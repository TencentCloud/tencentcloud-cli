**Example 1: 文件通道-获取下载URL**

文件通道-获取下载URL

Input: 

```
tccli ioa DescribeDownloadURL --cli-unfold-argument  \
    --Mid E6332B3A194BEAB6949156337DB97DCD5F22986B \
    --RandomNumber 123abc \
    --DownloadTimestamp 1682674961 \
    --SignatureInfo 4dfde3492988abf1cbaa1b7591d467776ed8f69090dbec37fd01d2a9736fd246 \
    --DownloadFile linux_process_mgr.pdf \
    --IgnoreTenant True
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVkIjoiMjAyMy0wNC0yOCAxODo0MzoyOCIsIm1pZCI6IkU2MzMyQjNBMTk0QkVBQjY5NDkxNTYzMzdEQjk3RENENUYyMjk4NkIifQ.AEpuEG1gX2eqItYKgO4e0AIoTnVoN5t23o8P0jiUbLU",
            "DownloadURL": "https://ioa-dev-2-1258344699.cos.accelerate.myqcloud.com/linux_process_mgr.pdf?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1682675008%3B1682678608&q-key-time=1682675008%3B1682678608&q-header-list=host&q-url-param-list=&q-signature=41d1abe1e2fb4efdbb5d381736e84cf3861aed6a",
            "ExpireAt": "2023-04-28 18:43:28"
        },
        "RequestId": "74818cbc-3482-44b3-81d9-c2504be41a5d"
    }
}
```

