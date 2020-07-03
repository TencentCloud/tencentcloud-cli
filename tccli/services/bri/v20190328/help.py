# -*- coding: utf-8 -*-
DESC = "bri-2019-03-28"
INFO = {
  "DescribeBRI": {
    "params": [
      {
        "name": "RequestData",
        "desc": "业务风险情报请求体"
      },
      {
        "name": "ResourceId",
        "desc": "客户用于计费的资源ID"
      }
    ],
    "desc": "输入业务名 (bri_num, bri_dev, bri_ip, bri_apk, bri_url 五种之一)  及其 相应字段, 获取业务风险分数和标签。\n\n当业务名为bri_num时，必须填PhoneNumber字段.\n\n当业务名为bri_dev时, 必须填Imei字段.\n\n当业务名为bri_ip时，必须填IP字段.\n\n当业务名为bri_apk时，必须填 (PackageName,CertMd5,FileSize) 三个字段 或者 FileMd5一个字段.\n\n当业务名为bri_url时，必须填Url字段.\n\n当业务名为bri_social时，必须填QQ和Wechat字段两者其中一个或者两个."
  }
}