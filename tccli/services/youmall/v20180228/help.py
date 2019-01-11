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
      },
      {
        "name": "PersonType",
        "desc": "身份类型(0表示普通顾客，1 白名单，2 表示黑名单）"
      }
    ],
    "desc": "指定门店获取所有顾客详情列表，包含客户ID、图片、年龄、性别"
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
  "DescribeZoneFlowAgeInfoByZoneId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "ZoneId",
        "desc": "区域ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      }
    ],
    "desc": "获取指定区域人流各年龄占比"
  },
  "CreateAccount": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "Name",
        "desc": "账号名；需要是手机号"
      },
      {
        "name": "Password",
        "desc": "密码；需要是(`~!@#$%^&*()_+=-）中的至少两种且八位以上"
      },
      {
        "name": "ShopCode",
        "desc": "客户门店编码"
      },
      {
        "name": "Remark",
        "desc": "备注说明; 30个字符以内"
      }
    ],
    "desc": "创建集团门店管理员账号"
  },
  "DescribeZoneFlowAndStayTime": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
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
      }
    ],
    "desc": "获取区域人流和停留时间"
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
        "name": "Offset",
        "desc": "偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit"
      },
      {
        "name": "Limit",
        "desc": "Limit:每页的数据项，最大100，超过100会被强制指定为100"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd，已废弃，请使用StartDateTime"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd，已废弃，请使用EndDateTime"
      },
      {
        "name": "PictureExpires",
        "desc": "图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）"
      },
      {
        "name": "StartDateTime",
        "desc": "开始时间，格式yyyy-MM-dd HH:mm:ss"
      },
      {
        "name": "EndDateTime",
        "desc": "结束时间，格式yyyy-MM-dd HH:mm:ss"
      }
    ],
    "desc": "获取门店指定时间范围内的所有用户到访信息记录，支持的时间范围：过去365天，含当天。"
  },
  "DescribeZoneFlowHourlyByZoneId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "ZoneId",
        "desc": "区域ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      }
    ],
    "desc": "获取指定区域分时客流量"
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
      },
      {
        "name": "PictureExpires",
        "desc": "图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）"
      }
    ],
    "desc": "通过DescribeCameraPerson接口上报的收银台身份ID查询顾客的FaceID。查询最佳时间为收银台上报的次日1点后。"
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
  },
  "DescribePersonInfoByFacePicture": {
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
        "name": "Picture",
        "desc": "人脸图片BASE编码"
      }
    ],
    "desc": "通过上传人脸图片检索系统face id、顾客身份信息及底图"
  },
  "CreateFacePicture": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "PersonType",
        "desc": "人物类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）"
      },
      {
        "name": "Picture",
        "desc": "图片BASE编码"
      },
      {
        "name": "PictureName",
        "desc": "图片名称"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID，如果不填表示操作集团身份库"
      },
      {
        "name": "IsForceUpload",
        "desc": "是否强制更新：为ture时会为用户创建一个新的指定PersonType的身份;目前这个参数已废弃，可不传"
      }
    ],
    "desc": "通过上传指定规格的人脸图片，创建黑名单用户或者白名单用户。"
  },
  "DescribeZoneFlowGenderAvrStayTimeByZoneId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "ZoneId",
        "desc": "区域ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      }
    ],
    "desc": "获取指定区域不同年龄段男女平均停留时间"
  },
  "DescribeTrajectoryData": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
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
        "name": "Limit",
        "desc": "限制返回数据的最大条数，最大 400（负数代为 400）"
      },
      {
        "name": "Gender",
        "desc": "顾客性别顾虑，0是男，1是女，其它代表不分性别"
      }
    ],
    "desc": "获取动线轨迹信息"
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
  "DescribePersonTrace": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "PersonId",
        "desc": "客户编码"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      }
    ],
    "desc": "输出开始时间到结束时间段内的进出场数据。"
  },
  "DescribeZoneFlowDailyByZoneId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "ZoneId",
        "desc": "区域ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      }
    ],
    "desc": "获取指定区域每日客流量"
  },
  "DescribePersonArrivedMall": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "PersonId",
        "desc": "客户编码"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      }
    ],
    "desc": "输出开始时间到结束时间段内的进出场数据。不做按天聚合的情况下，每次进出场，产生一条进出场数据。\n\n"
  },
  "ModifyPersonType": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "门店ID"
      },
      {
        "name": "PersonId",
        "desc": "顾客ID"
      },
      {
        "name": "PersonType",
        "desc": "身份类型(0表示普通顾客，1 白名单，2 表示黑名单）"
      },
      {
        "name": "PersonSubType",
        "desc": "身份子类型:\nPersonType=0时(普通顾客)，0普通顾客\nPersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册会员，5VIP用户\nPersonType=2时(黑名单)，0普通黑名单，1小偷)"
      }
    ],
    "desc": "修改顾客身份类型接口"
  },
  "DescribeClusterPersonArrivedMall": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "PersonId",
        "desc": "客户编码"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      }
    ],
    "desc": "输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。停留时间为多次进出场的停留时间之和。"
  },
  "DescribePersonTraceDetail": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "PersonId",
        "desc": "客户编码"
      },
      {
        "name": "TraceId",
        "desc": "轨迹编码"
      }
    ],
    "desc": "查询客户单次到场轨迹明细"
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
  "ModifyPersonFeatureInfo": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "PersonId",
        "desc": "需要修改的顾客id"
      },
      {
        "name": "Picture",
        "desc": "图片BASE编码"
      },
      {
        "name": "PictureName",
        "desc": "图片名称（尽量不要重复）"
      },
      {
        "name": "PersonType",
        "desc": "人物类型，仅能操作黑白名单顾客（1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID，如果不填表示操作集团身份库"
      }
    ],
    "desc": "支持修改黑白名单类型的顾客特征"
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
  "DeletePersonFeature": {
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
        "name": "PersonId",
        "desc": "顾客ID"
      }
    ],
    "desc": "删除顾客特征，仅支持删除黑名单或者白名单用户特征。"
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
  "DescribeZoneFlowGenderInfoByZoneId": {
    "params": [
      {
        "name": "CompanyId",
        "desc": "集团ID"
      },
      {
        "name": "ShopId",
        "desc": "店铺ID"
      },
      {
        "name": "ZoneId",
        "desc": "区域ID"
      },
      {
        "name": "StartDate",
        "desc": "开始日期，格式yyyy-MM-dd"
      },
      {
        "name": "EndDate",
        "desc": "结束日期，格式yyyy-MM-dd"
      }
    ],
    "desc": "获取指定区域性别占比"
  },
  "DescribeClusterPersonTrace": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "PersonId",
        "desc": "客户编码"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      }
    ],
    "desc": "输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。"
  },
  "DescribePerson": {
    "params": [
      {
        "name": "MallId",
        "desc": "卖场编码"
      },
      {
        "name": "Offset",
        "desc": "查询偏移"
      },
      {
        "name": "Limit",
        "desc": "查询数量，默认20，最大查询数量100"
      }
    ],
    "desc": "查询指定某一卖场的用户信息"
  }
}