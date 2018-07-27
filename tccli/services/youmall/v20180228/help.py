# -*- coding: utf-8 -*-
DESC = "youmall-2018-02-28"
INFO = {
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
      }
    ],
    "desc": "指定门店获取所有顾客详情列表，包含客户ID、图片、年龄、性别"
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
  }
}