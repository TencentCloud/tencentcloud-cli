**Example 1: GetImagePreview**

获取图片预览临时链接

Input: 

```
tccli lke GetImagePreview --cli-unfold-argument  \
    --AppBizId 1908065244491808768 \
    --TypeKey realtime \
    --CosUrl /corp/1905507781330599936/1908065244491808768/image/EeAbAqqyMyrBxbQCxmVP-1922140828205624448.png
```

Output: 
```
{
    "Response": {
        "Url": "https://lke-realtime-1251316161.cos.ap-guangzhou.myqcloud.com/%2Fcorp/1905507781330599936/1918149601548566528/image/PgPPcltWcVeisEztekBJ-1918149669236768768.png?q-sign-algorithm=sha1&q-ak=AKIDqQ2UCeGDtjVkjauVp8NM1czNWPAgwvhF&q-sign-time=1747109286%3B1747111086&q-key-time=1747109286%3B1747111086&q-header-list=host&q-url-param-list=&q-signature=49ede7eb87d09a6126fb15d0d084f23fe7c356de",
        "RequestId": "143a9f30-a21c-4eb3-af82-ccacd4cdcbfd"
    }
}
```

