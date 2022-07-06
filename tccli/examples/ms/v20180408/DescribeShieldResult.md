**Example 1: 查询加固结果**

通过唯一标识获取加固的结果，唯一标识ItemId通过请求加固接口返回

Input: 

```
tccli ms DescribeShieldResult --cli-unfold-argument  \
    --ItemId 1shi2e-2387hjgus
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "TaskStatus": 0,
        "StatusDesc": "",
        "StatusRef": "",
        "AppDetailInfo": {
            "AppName": "微信",
            "AppPkgName": "com.tencent.mm",
            "AppVersion": "1.0",
            "AppSize": 1234565,
            "AppMd5": "dd5b29a800246d7089febf228286d901",
            "FileName": "xx",
            "AppIconUrl": "https://example.com/1.png"
        },
        "ShieldInfo": {
            "ShieldCode": 1,
            "ShieldSize": 1024,
            "ShieldMd5": "25787jhids",
            "AppUrl": "https://example.com/1.apk",
            "TaskTime": 1245478744,
            "ItemId": "hji452-huhsxqwq1212",
            "ServiceEdition": "xx"
        }
    }
}
```

**Example 2: 返回**



Input: 

```
tccli ms DescribeShieldResult --cli-unfold-argument  \
    --ItemId 0b5465636cac72bb98e24b6aa4f4c488
```

Output: 
```
{
    "Response": {
        "AppDetailInfo": {
            "AppIconUrl": "https://ms-shield-logo-1251001047-1252181758.cosgz.myqcloud.com/0/881ac0a49b3ae9967022217730cc0da8/onetools.apklogo",
            "AppMd5": "881ac0a49b3ae9967022217730cc0da8",
            "AppName": "一个木函",
            "AppPkgName": "com.One.WoodenLetter",
            "AppSize": 4743475,
            "AppVersion": "7.8.1",
            "FileName": "onetools.apk"
        },
        "RequestId": "5bcf07de-03fe-4f8b-b859-9b7b47316045",
        "ShieldInfo": {
            "AppUrl": "https://ms-shield-1251001047-1252181758.cos.ap-guangzhou.myqcloud.com/encrypt_dist/881ac0a49b3ae9967022217730cc0da8.20220412121930.apk?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID2oNhcKawrmdDWc9eO1TheMnxsZeT983h%26q-sign-time%3D1650339239%3B1650342839%26q-key-time%3D1650339239%3B1650342839%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Dfbf5764a72c6e42c97aeb53c6cf6e6b85f6e7689%00",
            "ItemId": "0b5465636cac72bb98e24b6aa4f4c488",
            "ServiceEdition": "basic",
            "ShieldCode": 0,
            "ShieldMd5": "5c5d992097727c2f9789fea97441bd52",
            "ShieldSize": 5373548,
            "TaskTime": 1649737137
        },
        "StatusDesc": "",
        "StatusRef": "",
        "TaskStatus": 1
    }
}
```

