**Example 1: 获取英文分类**



Input: 

```
tccli tencentcloudintl DescribeCategoryListByLang --cli-unfold-argument  \
    --Lang en
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BackgroundUrl": "https://main.qcloudimg.com/raw/e497194e982667f67523d0d2099cc487.png",
                "Children": [],
                "GroupId": 1,
                "IconUrl": "https://cloudcache.tencent-cloud.com/open_proj/proj_qcloud_v2/international/doc/css/img/icon/icon-compute.svg",
                "Id": 211,
                "Lang": "en",
                "Pid": 0,
                "ProductSwitch": 0,
                "Slug": "compute",
                "Switch": 1,
                "Title": "Compute",
                "Url": "",
                "Weight": 401
            }
        ],
        "RequestId": "0b09579d-0756-4b17-aa83-c62b95e4d943"
    }
}
```

