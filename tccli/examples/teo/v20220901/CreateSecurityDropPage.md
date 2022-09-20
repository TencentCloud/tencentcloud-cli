**Example 1: 使用在线url创建自定义拦截页面**

当想通过在线URL上传为自定义页面时：
将url地址进行urlencode，填入Content字段，并且Type填入url。

Input: 

```
tccli teo CreateSecurityDropPage --cli-unfold-argument  \
    --Content https%3A%2F%2Fcloud.tencent.com%2Fabout \
    --Entity www.example.com \
    --Name hello.html \
    --ZoneId zone-abcdefg \
    --Type url \
    --Module waf
```

Output: 
```
{
    "Response": {
        "PageId": 1234546,
        "RequestId": "13j90e13-kf204fk0-wf0k0af"
    }
}
```

**Example 2: 使用文件内容创建自定义拦截页面**

当想通过本地文件上传为自定义页面时：
将页面文件内容进行urlencode，填入Content字段，并且Type填入file。

Input: 

```
tccli teo CreateSecurityDropPage --cli-unfold-argument  \
    --Content %3Chtml%3E%0Ahello%20world%2C%20uuid%3A%20%3A%3AEO_REQ_ID%0A%3C%2Fhtml%3E \
    --Entity www.example.com \
    --Name hello.html \
    --ZoneId zone-abcdefg \
    --Type file \
    --Module waf
```

Output: 
```
{
    "Response": {
        "PageId": 1234546,
        "RequestId": "wwefoj-ewij23rkf-34t98jrg"
    }
}
```

