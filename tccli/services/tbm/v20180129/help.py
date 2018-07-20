# -*- coding: utf-8 -*-
DESC = "tbm-2018-01-29"
INFO = {
  "DescribeUserPortrait": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      }
    ],
    "desc": "通过分析洞察参与过品牌媒体互动的用户，比如公开发表品牌的新闻评论、在公开社交渠道发表过对品牌的评价观点等用户，返回用户的画像属性分布，例如性别、年龄、地域、喜爱的明星、喜爱的影视。"
  },
  "DescribeBrandPosComments": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      },
      {
        "name": "Limit",
        "desc": "查询条数上限，默认20"
      },
      {
        "name": "Offset",
        "desc": "查询偏移，从0开始"
      }
    ],
    "desc": "通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌热门好评观点列表。"
  },
  "DescribeBrandMediaReport": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      }
    ],
    "desc": "监测品牌关键词出现在媒体网站（新闻媒体、网络门户、政府网站、微信公众号、天天快报等）发布资讯标题和正文中的报道数。按天输出结果。"
  },
  "DescribeBrandNegComments": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      },
      {
        "name": "Limit",
        "desc": "查询条数上限，默认20"
      },
      {
        "name": "Offset",
        "desc": "查询偏移，默认从0开始"
      }
    ],
    "desc": "通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌热门差评观点列表。"
  },
  "DescribeBrandSocialReport": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      }
    ],
    "desc": "监测品牌关键词出现在微博、QQ兴趣部落、论坛、博客等个人公开贡献资讯中的条数。按天输出数据结果。"
  },
  "DescribeBrandSocialOpinion": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "检索开始时间"
      },
      {
        "name": "EndDate",
        "desc": "检索结束时间"
      },
      {
        "name": "Offset",
        "desc": "查询偏移，默认从0开始"
      },
      {
        "name": "Limit",
        "desc": "查询条数上限，默认20"
      },
      {
        "name": "ShowList",
        "desc": "列表显示标记，若为true，则返回文章列表详情"
      }
    ],
    "desc": "检测品牌关键词出现在微博、QQ兴趣部落、论坛、博客等个人公开贡献资讯中的内容，每天聚合近30天热度最高的观点列表。"
  },
  "DescribeIndustryNews": {
    "params": [
      {
        "name": "IndustryId",
        "desc": "行业ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      },
      {
        "name": "ShowList",
        "desc": "是否显示列表，若为 true，则返回文章列表"
      },
      {
        "name": "Offset",
        "desc": "查询偏移，默认从0开始"
      },
      {
        "name": "Limit",
        "desc": "查询条数上限，默认20"
      }
    ],
    "desc": "根据客户定制的行业关键词，监测关键词出现在媒体网站（新闻媒体、网络门户、政府网站、微信公众号、天天快报等）发布资讯标题和正文中的报道数，以及文章列表、来源渠道、作者、发布时间等。"
  },
  "DescribeBrandCommentCount": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始日期"
      },
      {
        "name": "EndDate",
        "desc": "查询结束日期"
      }
    ],
    "desc": "通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌好评与差评评价条数，按天输出结果。"
  },
  "DescribeBrandExposure": {
    "params": [
      {
        "name": "BrandId",
        "desc": "品牌ID"
      },
      {
        "name": "StartDate",
        "desc": "查询开始时间"
      },
      {
        "name": "EndDate",
        "desc": "查询结束时间"
      }
    ],
    "desc": "监测品牌关键词命中文章标题或全文的文章篇数，按天输出数据。"
  }
}