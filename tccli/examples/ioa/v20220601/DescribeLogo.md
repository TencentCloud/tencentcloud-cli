**Example 1: 获取自定义Logo信息**

一进入界面加载接口，没有配置过自定义信息，返回一个空的数组。data对象里面的ResourceCommonValue，saas环境返回的是一个cos链接

Input: 

```
tccli ioa DescribeLogo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ResourceCommonName": "en_title",
                    "ResourceCommonValue": "Test-B aa iOA"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_32.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_32.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=ce471e8d44c0c5b5dfb1b082b3943428a96600d5"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_64.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_64.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=dd81a52899a747414666175cb5dcf12fdf6ea631"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_128.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_128.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=10dfe7674efd96c8cdf7ec2a364bdb5e97c0eb37"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_256.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_256.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=e3e72a78bd72a65c5ef3aec6f759d114da327c00"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_512.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_512.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=a9d44c5f2108bca9c7c523f1134aaafc4dc85996"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_1024.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_1024.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=5fe3dca735b245c0fab5c2f88c4b480415ed3aa8"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_256.ico",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_256.ico?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=1c06e4209181d3205a3ead7efffe2ddd7bbf6774"
                },
                {
                    "ResourceCommonName": "logoIcon_white_16.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_white_16.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=b8323e6a6eb7580b1b1c17cba55078eb220ea012"
                },
                {
                    "ResourceCommonName": "logoIcon_white_32.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_white_32.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=cade8487935310eeab20270dea016c34ff280f9b"
                },
                {
                    "ResourceCommonName": "logoIcon_white_64.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_white_64.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=59386df88bdd8e624b0d0ce0ef74025b48e3ced8"
                },
                {
                    "ResourceCommonName": "logoIcon_white_128.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_white_128.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=f91126218c316d8c36a7185199bfb04330f224b1"
                },
                {
                    "ResourceCommonName": "logoIcon_white_256.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_white_256.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=87b5a1ed8943ce1131dbafbe0f410396277d0138"
                },
                {
                    "ResourceCommonName": "logoIcon_black_16.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_black_16.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=f4a858e4a4af0e6115f7fbdb63560f8535f2d2d4"
                },
                {
                    "ResourceCommonName": "logoIcon_black_32.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_black_32.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=44295e16d89a09b9e86e90827e68813d6cf3fc95"
                },
                {
                    "ResourceCommonName": "logoIcon_black_64.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_black_64.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=d3de1a8d664f4881c7db8fe9d83437a631badd31"
                },
                {
                    "ResourceCommonName": "logoIcon_black_128.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_black_128.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=e8a3a53d3c7c0f1bc543df59a012c508097be9e7"
                },
                {
                    "ResourceCommonName": "logoIcon_black_256.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_black_256.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=55b713d12f701f1e17677138185a36dc653bf312"
                },
                {
                    "ResourceCommonName": "cn_title",
                    "ResourceCommonValue": "测试-B QQ iOA"
                },
                {
                    "ResourceCommonName": "logoIcon_colour_16.png",
                    "ResourceCommonValue": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/1300055735/web-open-api/logo/logoIcon_colour_16.png?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1679644321%3B1679647921&q-key-time=1679644321%3B1679647921&q-header-list=host&q-url-param-list=&q-signature=67e95442c1600992d25bd017cca4083f513b11a4"
                }
            ]
        },
        "RequestId": "b83e80cb-fd2d-43d8-bcdc-f08cd0a9167c"
    }
}
```

