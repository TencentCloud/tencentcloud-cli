**Example 1: 文件通道-获取上传URL**

文件通道-获取上传URL

Input: 

```
tccli ioa DescribeUploadURL --cli-unfold-argument  \
    --Mid E6332B3A194BEAB6949156337DB97DCD5F22986B \
    --RandomNumber 123abc \
    --UploadTimestamp 1682672361 \
    --SignatureInfo e5ee49b71de73f1cd3258aa2ff328cd968f0a292107f750145424c116025565c \
    --UploadFile linux_process_mgr.pdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "ExpireAt": "2023-04-28 18:18:02",
            "UploadToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVkIjoiMjAyMy0wNC0yOCAxODoxODowMiIsIm1pZCI6IkU2MzMyQjNBMTk0QkVBQjY5NDkxNTYzMzdEQjk3RENENUYyMjk4NkIifQ.k5vVS8b7OY-IIMkxb6tpfdtC3uNSBZcFHIrZVszxV3o",
            "UploadURL": "https://ioa-dev-2-1258344699.cos.accelerate.myqcloud.com/1300055726/linux_process_mgr.pdf?x-cos-security-token=WxUnD41j71Mj2BUW9vpXb1n3JobRy1oa02375b00ca956dec684ee49d8d5fcbfaTEv04Pb0PkYiLl-wvMqaqPjxr0mBvqJX8FA1809wMLLX2Ij8shZz60qzeQdbgbOaSfG6OW2VLQXpSodi-i5lj8A4kO4aRJ18yBQju2tqBRpURaEE7SOhPMTSaDIYHhJOvPRPZQ-ZzxTre6yVkJvuVgSvia1l7UefGxpFEn7roNzxCT7atGJDW2A3GKpR9Vyy1YN4MPKE4rnd_x2uKnTq7CJthZYiLdIW4_prI7d4liY-MY8ZMid7znYGsDsS4fwJwFDVVFWCI5bPKOeXoGmosKnsj-oJhVFp9gWnewYzzz7_SOYVKeFMuWzglR9FnDrXAv_nuB71tvmYLX_jlyhJzw&q-sign-algorithm=sha1&q-ak=AKIDTVIUtA1b64LPW7loutDyNsidrVGEmLNoU25pDpPhmF6v82jqb1YJnNWvxaMbRwcb&q-sign-time=1682673482%3B1682677082&q-key-time=1682673482%3B1682677082&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=5554a60a6df24617aff394f99300a7716dcd8dcc"
        },
        "RequestId": "1befc345-3d7c-403c-999a-04769caffe03"
    }
}
```

**Example 2: 文件通道 - 获取上传URL**

文件通道 - 获取上传URL

Input: 

```
tccli ioa DescribeUploadURL --cli-unfold-argument  \
    --Mid E6332B3A194BEAB6949156337DB97DCD5F22986B \
    --RandomNumber 123abc \
    --UploadTimestamp 1682673977 \
    --SignatureInfo e84bce28890cb459644ac3f10d5f0c070f3cb708f1dbf4b6ffca88559ec873b1 \
    --UploadFile linux_process_mgr.pdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "ExpireAt": "2023-04-28 18:26:45",
            "UploadToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmVkIjoiMjAyMy0wNC0yOCAxODoyNjo0NSIsIm1pZCI6IkU2MzMyQjNBMTk0QkVBQjY5NDkxNTYzMzdEQjk3RENENUYyMjk4NkIifQ.jLWmebkFM9iP4OXfEqICkO8B21HDspWztUfLEcJhMEg",
            "UploadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/251226898/linux_process_mgr.pdf?x-cos-security-token=mGHhhMsFxBPWqmq6t85B0Gq3Zvo9MuGa8f1b174a46a25a47c957a64333c9b6e3DFKX3CYyY2gIQdyPz2SqZkV4KRiPDpEMdNY-pxW-Ftq386W2UtBavjAVrxAV1ZFcbyk9zKcTnx1eZiIO2qPRVX4JRk-sHIho0dtzxma45ZvVwUzuAJdBz8aiBYAeXXZ1-KdedoiIhJ_rEQxdMO0KfdA1xQjBysVOsb1PQy3yS_HT7AjtIfjSsLCp7h5Zb7-OL2NBFyXvnV1HMOeMJOxA5TDb005iGYNj4AEhJNtnQhpcC4plOMybsDMqklrYQ_ZIaHG7p9ADehjZgiLazUaCS7tgyiuvNL_Xb0b22Uw1DzIxC9Ufv9hc0TAlQNqEGk-N7-Hr9IiHCL_OiQXBKN21ew&q-sign-algorithm=sha1&q-ak=AKID4FmvYx0xj7VoyeHGq8iIUwAMDFiw4WQXA_8pTk26lV5VNJY2h8wkanF4VJ3RgR8K&q-sign-time=1682674005%3B1682677605&q-key-time=1682674005%3B1682677605&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=9401c75737660f353b2e52b1c4d29a78763acd59"
        },
        "RequestId": "10bdd94d-8e9e-4b46-9626-ed479d3a93b6"
    }
}
```

