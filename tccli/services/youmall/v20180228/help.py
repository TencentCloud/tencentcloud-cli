# -*- coding: utf-8 -*-
DESC = "youmall-2018-02-28"
INFO = {
  "DescribeCameraPerson": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "优mall集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "ShopId",
        "desc": "优mall店铺id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "CameraId",
        "desc": "摄像头id"
      },
      {
        "name": "StartTime",
        "desc": "拉取开始时间戳，单位秒"
      },
      {
        "name": "EndTime",
        "desc": "拉取结束时间戳，单位秒，不超过StartTime+10秒，超过默认为StartTime+10"
      },
      {
        "name": "PosId",
        "desc": "pos机id"
      },
      {
        "name": "Num",
        "desc": "拉取图片数，默认为1，最大为3"
      },
      {
        "name": "IsNeedPic",
        "desc": "是否需要base64的图片，0-不需要，1-需要，默认0"
      }
    ],
    "desc": "通过指定设备ID和指定时段，获取该时段内中收银台摄像设备抓取到顾客头像及身份ID"
  },
  "DescribePersonInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "公司ID"
      },
      {
        "name": "ShopId",
        "desc": "门店ID"
      },
      {
        "name": "StartPersonId",
        "desc": "起始ID，第一次拉取时StartPersonId传0，后续送入的值为上一页最后一条数据项的PersonId"
      },
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      },
      {
        "name": "PictureExpires",
        "desc": "图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）"
      }
    ],
    "desc": "指定门店获取所有顾客详情列表，包含客户ID、图片、年龄、性别"
  },
  "DescribeFaceIdByTempId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "优mall集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "ShopId",
        "desc": "优mall店铺id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "TempId",
        "desc": "临时id"
      },
      {
        "name": "CameraId",
        "desc": "摄像头id"
      },
      {
        "name": "PosId",
        "desc": "pos机id"
      }
    ],
    "desc": "通过DescribeCameraPerson接口上报的收银台身份ID查询顾客的FaceID。查询最佳时间为收银台上报的次日1点后。"
  },
  "DescribeHistoryNetworkInfo": {
    "params": [
      {
        "name": "Time",
        "desc": "请求时间戳"
      },
      {
        "name": "CompanyId",
        "desc": "优mall集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "ShopId",
        "desc": "优mall店铺id，通过\"指定身份标识获取客户门店列表\"接口获取，为0则拉取集团全部店铺当前"
      },
      {
        "name": "StartDay",
        "desc": "拉取开始日期，格式：2018-09-05"
      },
      {
        "name": "EndDay",
        "desc": "拉取结束日期，格式L:2018-09-05，超过StartDay 90天，按StartDay+90天算"
      },
      {
        "name": "Limit",
        "desc": "拉取条数，默认10"
      },
      {
        "name": "Offset",
        "desc": "拉取偏移，返回offset之后的数据"
      }
    ],
    "desc": "返回当前门店历史网络状态数据"
  },
  "DescribeNetworkInfo": {
    "params": [
      {
        "name": "Time",
        "desc": "请求时间戳"
      },
      {
        "name": "CompanyId",
        "desc": "优mall集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "ShopId",
        "desc": "优mall店铺id，通过\"指定身份标识获取客户门店列表\"接口获取，不填则拉取集团全部店铺当前"
      }
    ],
    "desc": "返回当前门店最新网络状态数据"
  },
  "DescribeShopHourTrafficInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "公司ID"
      },
      {
        "name": "ShopId",
        "desc": "门店ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式：yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式：yyyy-MM-dd"
      },
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      }
    ],
    "desc": "按小时提供查询日期范围内门店的每天每小时累计客流人数数据，支持的时间范围：过去365天，含当天。"
  },
  "ModifyPersonTagInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "优mall集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "ShopId",
        "desc": "优mall店铺id，通过\"指定身份标识获取客户门店列表\"接口获取，为0则拉取集团全部店铺当前"
      },
      {
        "name": "Tags",
        "desc": "需要设置的顾客信息，批量设置最大为10个"
      }
    ],
    "desc": "标记到店顾客的身份类型，例如黑名单、白名单等\n"
  },
  "DescribeZoneTrafficInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "公司ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      },
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      }
    ],
    "desc": "按天提供查询日期范围内，客户指定门店下的所有区域（优Mall部署时已配置区域）的累计客流人次和平均停留时间。支持的时间范围：过去365天，含当天。"
  },
  "DescribeShopInfo": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      }
    ],
    "desc": "根据客户身份标识获取客户下所有的门店信息列表"
  },
  "DescribePersonVisitInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "公司ID"
      },
      {
        "name": "ShopId",
        "desc": "门店ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      },
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      },
      {
        "name": "PictureExpires",
        "desc": "图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）"
      }
    ],
    "desc": "获取门店指定时间范围内的所有用户到访信息记录，支持的时间范围：过去365天，含当天。"
  },
  "RegisterCallback": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团id，通过\"指定身份标识获取客户门店列表\"接口获取"
      },
      {
        "name": "BackUrl",
        "desc": "通知回调地址，完整url，示例（http://youmall.tencentcloudapi.com/）"
      },
      {
        "name": "Time",
        "desc": "请求时间戳"
      },
      {
        "name": "NeedFacePic",
        "desc": "是否需要顾客图片，1-需要图片，其它-不需要图片"
      }
    ],
    "desc": "调用本接口在优Mall中注册自己集团的到店通知回调接口地址，接口协议为HTTP或HTTPS。注册后，若集团有特殊身份（例如老客）到店通知，优Mall后台将主动将到店信息push给该接口"
  },
  "DescribeShopTrafficInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "公司ID"
      },
      {
        "name": "ShopId",
        "desc": "门店ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "介绍日期，格式yyyy-MM-dd"
      },
      {
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      }
    ],
    "desc": "按天提供查询日期范围内门店的单日累计客流人数，支持的时间范围：过去365天，含当天。"
  }
}