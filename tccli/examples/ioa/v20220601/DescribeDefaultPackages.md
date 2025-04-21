**Example 1: 示例**

获取下载包

Input: 

```
tccli ioa DescribeDefaultPackages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4872bbd0-bffb-4c86-a029-7a4160ad2fff",
        "Data": [
            {
                "OsType": "mac",
                "Version": "208.0.5476.61000",
                "Url": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/data/services/pcmgr_enterprise/public/www/public/store/package/resource/1300223957/PCMgr_Setup_Mac.pkg?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1672038774%3B1672042374&q-key-time=1672038774%3B1672042374&q-header-list=host&q-url-param-list=&q-signature=c34bcb4a8824431a02421619c98f3f1fcf2cccb6"
            },
            {
                "OsType": "android",
                "Version": "208.0.3096.62000",
                "Url": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/data/services/pcmgr_enterprise/public/www/public/store/package/resource/1300223957/android_qrcode.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1672038774%3B1672042374&q-key-time=1672038774%3B1672042374&q-header-list=host&q-url-param-list=&q-signature=ccbce85ef7ef4727b606ce61846630df06ad3383"
            }
        ]
    }
}
```

